import os
# TODO - should finish this sometime
from typing import List, Union, Dict, Tuple, Any, Set
from dataset_utils.sqlite import get_or_create, ConnectMode, connect
from dataset_utils.buffered_writer import BufferedTableWriter, ConflictChecker
import os
import dataset
from collections import defaultdict
from pypika import Table, Query


def chunks(lst, n):
    # https://stackoverflow.com/a/312464
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class ScoreCache(object):
    def __init__(self, dbpath, table_name: str, rel_from: str):
        # model id is model_name + model version
        assert os.path.abspath(dbpath) == dbpath, f'error: please pass in an absolute path: {dbpath} vs {os.path.abspath(dbpath)}'
        dne = not os.path.exists(dbpath)
        self.dbpath = dbpath
        self.table_name = table_name
        self.rel_from = rel_from
        self.db, self.table = get_or_create(
            self.dbpath, self.table_name, primary_id='path', types={'path': 'string'},
            mode=ConnectMode.WAL)
        # assert self.table_name in self.db

    def create_indicies(self):
        assert isinstance(self.table, dataset.Table)
        for col in self.table.columns:
            # NOTE: the below code only creates the index if it doesn't already exist
            self.table.create_index([col])

    def set_multiple(self, d: Dict[str, Dict[str, float]]):
        b = BufferedTableWriter(self.table, key_column='path', key_conflicts=ConflictChecker.OVERWRITE)
        for path, scores in d.items():
            assert isinstance(scores, dict), f'error scores is not a dict: {str(d)}'
            assert isinstance(path, str), f'path is not a string: {str(path)}'
            assert os.path.isabs(path), f'error: {path} is not an abs path'
            row: Dict[str, Any] = scores.copy()
            max_all = 0.0
            max_per = defaultdict(float)
            for label, score in scores.items():
                assert isinstance(score, float), f'Error contains non-floats: {str(scores)}'
                max_all = max(max_all, score)
                label_prefix = 'max_' + label.split('_')[0]
                max_per[label_prefix] = max(max_per[label_prefix], score)

            for label, score in max_per.items():
                row[label] = score

            row['max_all'] = max_all
            relpath = os.path.relpath(path, self.rel_from)
            row['path'] = relpath
            row['parent_folder'] = relpath.split('/')[0]
            b.insert(row)
        b.force_flush()
        self.create_indicies()

    def labels(self):
        result = []
        for col in self.table.columns:
            if col in ('parent_folder', 'path'):
                continue
            result.append(col)
        return result

    def count(self, label, threshold):
        params = {
            'label': label,
            'threshold': {
                '>=': threshold
            }
        }
        return self.table.count(**params)

    def top_predictions(
            self, target_class: str, any_path_prefix=None, none_path_prefix=None, folders=None, not_folders=None,
            order_by='default', order='desc', page=0, limit=10000,
            score_filter=None
    ) -> List[Dict[str, Any]]:
        if order_by in ('default', None):
            order_by = target_class
        if isinstance(folders, str):
            folders = [folders]
        assert order in ('desc', 'asc')
        results = []
        offset = page * limit
        import logging
        logging.error(f'order_by: {order_by}')
        logging.error(f'limit: {limit}')
        logging.error(f'offset: {offset}')
        from pypika import Table, Query, Order, Criterion
        ctable = Table(self.table_name)
        q = Query.from_(ctable).select(ctable.star)
        assert folders or not_folders, 'at least one needs to be set'
        assert not (folders and not_folders), 'folders and not_folders cannot be set'
        if folders:
            q = q.where(ctable.parent_folder.isin(folders))
        else:
            assert not_folders
            q = q.where(ctable.parent_folder.notin(not_folders))

        if score_filter is not None:
            isinstance(score_filter, list)
            for e in score_filter:
                assert len(e) == 3
                col, op, val = e
                if op == '>=':
                    q = q.where(getattr(ctable, col).gte(val))
                elif op == '<=':
                    q = q.where(getattr(ctable, col).lte(val))
                else:
                    raise Exception(f'Unknown operator: {op}')

        if any_path_prefix:
            if isinstance(any_path_prefix, str):
                any_path_prefix = [any_path_prefix]
            assert isinstance(any_path_prefix, list)
            criterions = []
            for path_prefix in any_path_prefix:
                assert isinstance(path_prefix, str)
                # either of the two criterions are equivalent...not sure which one is faster
                #q = q.where(ctable.path.glob(path_prefix + '*'))
                criterions.append(ctable.path.glob(path_prefix + '*'))
                # criterions.append(tag_table.path.glob(f'{folder}/*'))
            q = q.where(Criterion.any(criterions))

        ###### START MONKEY PATCH #####
        # until this PR gets merged:
        # https://github.com/kayak/pypika/pull/586/files

        from pypika.terms import Term, BasicCriterion, Comparator

        class Matching(Comparator):
            not_like = " NOT LIKE "
            like = " LIKE "
            not_ilike = " NOT ILIKE "
            ilike = " ILIKE "
            regex = " REGEX "
            bin_regex = " REGEX BINARY "
            as_of = " AS OF "
            glob = " GLOB "
            not_glob = " NOT GLOB "

        def not_glob(local_self, expr: str):
            return BasicCriterion(Matching.not_glob, local_self, Term.wrap_constant(expr))
        Term.not_glob = not_glob

        ###### END MONKEY PATCH #####

        if none_path_prefix:
            if isinstance(none_path_prefix, str):
                none_path_prefix = [none_path_prefix]
            criterions = []
            for path_prefix in none_path_prefix:
                assert isinstance(path_prefix, str)
                criterions.append(ctable.path.not_glob(path_prefix + '*'))
            q = q.where(Criterion.all(criterions))

        q = q.orderby(getattr(ctable, order_by), order=getattr(Order, order))
        # after the score, order by the path
        q = q.orderby(ctable.path)
        q = q.offset(offset)
        q = q.limit(limit)
        logging.error('should run: ' + str(q))
        #for row in self.table.find(parent_folder={'in': folders}, order_by=order_by, _offset=offset, _limit=limit):
        for row in self.db.query(str(q)):
            row['path'] = os.path.join(self.rel_from, row['path'])
            results.append(row)
        return results

    def table_counts(self):
        tmp_results = self.db.query(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}';")
        existing_tables = set()
        for row in tmp_results:
            existing_tables.add(row['name'])
        return existing_tables

    def get_multiple(self, paths: Union[List[str], str], default_score=None, order_by=None, limit=None) -> Tuple[Dict[str, Dict[str, Any]], List[str]]:
        existing_tables = self.table_counts()
        if self.table_name not in existing_tables:
            return {}, paths
        if isinstance(paths, str):
            paths = [paths]
        for path in paths:
            assert os.path.isabs(path)
        # we convert to relpath because we use it for everything
        relpaths = [os.path.relpath(path, self.rel_from) for path in paths]
        #import logging
        #logging.error('new paths: ' + str(paths))
        assert isinstance(relpaths, list)
        keys_set = set(paths)
        assert len(relpaths) == len(keys_set), 'Error: there are duplicate keys in your request'
        results = {}
        score_table = Table(self.table_name)

        for relpaths_chunk in chunks(relpaths, 10000):
            # we chunk the reads b/c there's a limit for how big a query can be
            q = Query.from_(score_table).select(
                score_table.star,
            )
            q = q.where(score_table.path.isin(relpaths_chunk))
            if order_by:
                q = q.orderby(order_by)
            q = q.limit(limit)
            for row in self.db.query(str(q)):
                relpath = row.pop('path')
                # row['path'] = relpath
                path = os.path.join(self.rel_from, relpath)
                parent_folder = row.pop('parent_folder')
                for label, score in row.items():
                    if score is None and default_score is not None:
                        score = default_score
                    assert isinstance(score, float), f'Error contains non-floats: {str(row)}'
                assert isinstance(row, dict)
                row['parent_folder'] = parent_folder
                row['path'] = relpath
                results[path] = row
        remaining = keys_set - set(results.keys())
        remaining = [os.path.join(self.rel_from, p) for p in remaining]
        assert len(results) + len(remaining) == len(relpaths)
        return results, remaining

