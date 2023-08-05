'''
Class for a bipartite network
'''
from pandas.core.indexes.base import InvalidIndexError
from tqdm.auto import tqdm
import numpy as np
# from numpy_groupies.aggregate_numpy import aggregate
import pandas as pd
from pandas import DataFrame, Int64Dtype
import networkx as nx
# from scipy.sparse.csgraph import connected_components
import warnings
import bipartitepandas as bpd
from bipartitepandas import col_order, update_dict, to_list, logger_init, col_dict_optional_cols, aggregate_transform

class BipartiteBase(DataFrame):
    '''
    Base class for BipartitePandas, where BipartitePandas gives a bipartite network of firms and workers. Contains generalized methods. Inherits from DataFrame.

    Arguments:
        *args: arguments for Pandas DataFrame
        columns_req (list): required columns (only put general column names for joint columns, e.g. put 'j' instead of 'j1', 'j2'; then put the joint columns in reference_dict)
        columns_opt (list): optional columns (only put general column names for joint columns, e.g. put 'g' instead of 'g1', 'g2'; then put the joint columns in reference_dict)
        columns_contig (dictionary): columns requiring contiguous ids linked to boolean of whether those ids are contiguous, or None if column(s) not included, e.g. {'i': False, 'j': False, 'g': None} (only put general column names for joint columns)
        reference_dict (dict): clarify which columns are associated with a general column name, e.g. {'i': 'i', 'j': ['j1', 'j2']}
        col_dtype_dict (dict): link column to datatype
        col_dict (dict or None): make data columns readable. Keep None if column names already correct
        include_id_reference_dict (bool): if True, create dictionary of Pandas dataframes linking original id values to contiguous id values
        **kwargs: keyword arguments for Pandas DataFrame
    '''
    _metadata = ['col_dict', 'reference_dict', 'id_reference_dict', 'col_dtype_dict', 'columns_req', 'columns_opt', 'columns_contig', 'default_cluster', 'dtype_dict', 'default_clean', 'connected', 'correct_cols', 'no_na', 'no_duplicates', 'i_t_unique'] # Attributes, required for Pandas inheritance

    def __init__(self, *args, columns_req=[], columns_opt=[], columns_contig=[], reference_dict={}, col_dtype_dict={}, col_dict=None, include_id_reference_dict=False, **kwargs):
        # Initialize DataFrame
        super().__init__(*args, **kwargs)

        # Start logger
        logger_init(self)
        # self.logger.info('initializing BipartiteBase object')

        if len(args) > 0 and isinstance(args[0], BipartiteBase): # Note that isinstance works for subclasses
            self._set_attributes(args[0], include_id_reference_dict)
        else:
            self.columns_req = ['i', 'j', 'y'] + columns_req
            self.columns_opt = ['g', 'm'] + columns_opt
            self.columns_contig = update_dict({'i': False, 'j': False, 'g': None}, columns_contig)
            self.reference_dict = update_dict({'i': 'i', 'm': 'm'}, reference_dict)
            self._reset_id_reference_dict(include_id_reference_dict) # Link original id values to contiguous id values
            self.col_dtype_dict = update_dict({'i': 'int', 'j': 'int', 'y': 'float', 't': 'int', 'g': 'int', 'm': 'int'}, col_dtype_dict)
            default_col_dict = {}
            for col in to_list(self.columns_req):
                for subcol in to_list(self.reference_dict[col]):
                    default_col_dict[subcol] = subcol
            for col in to_list(self.columns_opt):
                for subcol in to_list(self.reference_dict[col]):
                    default_col_dict[subcol] = None

            # Create self.col_dict
            self.col_dict = col_dict_optional_cols(default_col_dict, col_dict, self.columns, optional_cols=[self.reference_dict[col] for col in self.columns_opt])

            # Set attributes
            self._reset_attributes()

        self.default_cluster = {
            'measure_cdf': False, # If True, approximate firm-level income cdfs
            'measure_moments': False, # If True, approximate firm-level moments
            'cluster_KMeans': False, # If True, cluster using KMeans. Valid only if cluster_quantiles=False.
            'cluster_quantiles': False # If True, cluster using quantiles. Valid only if cluster_KMeans=False, measure_cdf=False, and measure_moments=True, and measuring only a single moment.
        }

        self.dtype_dict = {
            'int': ['int', 'int8', 'int16', 'int32', 'int64', 'Int64'],
            'float': ['float', 'float8', 'float16', 'float32', 'float64', 'float128', 'int', 'int8', 'int16', 'int32', 'int64', 'Int64'],
            'str': 'str'
        }

        self.default_clean = {
            'connectedness': 'connected', # When computing largest connected set of firms: if 'connected', keep observations in the largest connected set of firms; if 'biconnected', keep observations in the largest biconnected set of firms; if None, keep all observations
            'i_t_how': 'max', # When dropping i-t duplicates: if 'max', keep max paying job; if 'sum', sum over duplicate worker-firm-year observations, then take the highest paying worker-firm sum; if 'mean', average over duplicate worker-firm-year observations, then take the highest paying worker-firm average. Note that if multiple time and/or firm columns are included (as in event study format), then data is converted to long, cleaned, then reconverted to its original format
            'drop_multiples': False, # If True, rather than collapsing over spells, drop any spells with multiple observations (this is for computational efficiency when re-collapsing data for biconnected components)
            'data_validity': True, # If True, run data validity checks; much faster if set to False
            'copy': False # If False, avoid copying data when possible
        }

        # self.logger.info('BipartiteBase object initialized')

    @property
    def _constructor(self):
        '''
        For inheritance from Pandas.
        '''
        return BipartiteBase

    def copy(self):
        '''
        Copy.

        Returns:
            bdf_copy (BipartiteBase): copy of instance
        '''
        df_copy = DataFrame(self, copy=True)
        bdf_copy = self._constructor(df_copy)
        bdf_copy._set_attributes(self) # This copies attribute dictionaries, default copy does not

        return bdf_copy

    def summary(self):
        '''
        Print summary statistics.
        '''
        mean_wage = np.mean(self[self.reference_dict['y']].to_numpy())
        max_wage = np.max(self[self.reference_dict['y']].to_numpy())
        min_wage = np.min(self[self.reference_dict['y']].to_numpy())
        ret_str = 'format: ' + type(self).__name__ + '\n'
        ret_str += 'number of workers: ' + str(self.n_workers()) + '\n'
        ret_str += 'number of firms: ' + str(self.n_firms()) + '\n'
        ret_str += 'number of observations: ' + str(len(self)) + '\n'
        ret_str += 'mean wage: ' + str(mean_wage) + '\n'
        ret_str += 'max wage: ' + str(max_wage) + '\n'
        ret_str += 'min wage: ' + str(min_wage) + '\n'
        ret_str += 'connected (None if not ignoring connected set): ' + str(self.connected) + '\n'
        for contig_col, is_contig in self.columns_contig.items():
            ret_str += 'contiguous {} ids (None if not included): '.format(contig_col) + str(is_contig) + '\n'
        ret_str += 'correct column names and types: ' + str(self.correct_cols) + '\n'
        ret_str += 'no nans: ' + str(self.no_na) + '\n'
        ret_str += 'no duplicates: ' + str(self.no_duplicates) + '\n'
        ret_str += 'i-t (worker-year) observations unique (None if t column(s) not included): ' + str(self.i_t_unique) + '\n'

        print(ret_str)

    def n_workers(self):
        '''
        Get the number of unique workers.

        Returns:
            (int): number of unique workers
        '''
        return self['i'].nunique()

    def n_firms(self):
        '''
        Get the number of unique firms.

        Returns:
            (int): number of unique firms
        '''
        fid_lst = []
        for fid_col in to_list(self.reference_dict['j']):
            fid_lst += list(self[fid_col].unique())
        return len(set(fid_lst))

    def n_clusters(self):
        '''
        Get the number of unique clusters.

        Returns:
            (int or None): number of unique clusters, None if not clustered
        '''
        if not self._col_included('g'): # If cluster column not in dataframe
            return None
        cid_lst = []
        for g_col in to_list(self.reference_dict['g']):
            cid_lst += list(self[g_col].unique())
        return len(set(cid_lst))

    def original_ids(self, copy=True):
        '''
        Return self merged with original column ids.

        Arguments:
            copy (bool): if False, avoid copy

        Returns:
            (BipartiteBase or None): copy of self merged with original column ids, or None if id_reference_dict is empty
        '''
        frame = pd.DataFrame(self, copy=copy)
        if self.id_reference_dict:
            for id_col, reference_df in self.id_reference_dict.items():
                if len(reference_df) > 0: # Make sure non-empty
                    for id_subcol in to_list(self.reference_dict[id_col]):
                        try:
                            frame = frame.merge(reference_df[['original_ids', 'adjusted_ids_' + str(len(reference_df.columns) - 1)]].rename({'original_ids': 'original_' + id_subcol, 'adjusted_ids_' + str(len(reference_df.columns) - 1): id_subcol}, axis=1), how='left', on=id_subcol)
                        except TypeError: # Int64 error with NaNs
                            frame[id_col] = frame[id_col].astype('Int64')
                            frame = frame.merge(reference_df[['original_ids', 'adjusted_ids_' + str(len(reference_df.columns) - 1)]].rename({'original_ids': 'original_' + id_subcol, 'adjusted_ids_' + str(len(reference_df.columns) - 1): id_subcol}, axis=1), how='left', on=id_subcol)
                # else:
                #     # If no changes, just make original_id be the same as the current id
                #     for id_subcol in to_list(self.reference_dict[id_col]):
                #         frame['original_' + id_subcol] = frame[id_subcol]
            return frame
        else:
            warnings.warn('id_reference_dict is empty. Either your id columns are already correct, or you did not specify `include_id_reference_dict=True` when initializing your BipartitePandas object')

            return None

    def _set_attributes(self, frame, no_dict=False, include_id_reference_dict=False):
        '''
        Set class attributes to equal those of another BipartitePandas object.

        Arguments:
            frame (BipartitePandas): BipartitePandas object whose attributes to use
            no_dict (bool): if True, only set booleans, no dictionaries
            include_id_reference_dict (bool): if True, create dictionary of Pandas dataframes linking original id values to contiguous id values
        '''
        # Dictionaries
        if not no_dict:
            self.columns_req = frame.columns_req.copy()
            self.columns_opt = frame.columns_opt.copy()
            self.reference_dict = frame.reference_dict.copy()
            self.col_dtype_dict = frame.col_dtype_dict.copy()
            self.col_dict = frame.col_dict.copy()
        self.columns_contig = frame.columns_contig.copy() # Required, even if no_dict
        if frame.id_reference_dict:
            self.id_reference_dict = {}
            # Must do a deep copy
            for id_col, reference_df in frame.id_reference_dict.items():
                self.id_reference_dict[id_col] = reference_df.copy()
        else:
            # This is if the original dataframe DIDN'T have an id_reference_dict (but the new dataframe may or may not)
            self._reset_id_reference_dict(include_id_reference_dict)
        # # Logger
        # self.logger = frame.logger
        # Booleans
        self.connected = frame.connected # If False, not connected; if 'connected', all observations are in the largest connected set of firms; if 'biconnected' all observations are in the largest biconnected set of firms; if None, connectedness ignored
        self.correct_cols = frame.correct_cols # If True, column names are correct
        self.no_na = frame.no_na # If True, no NaN observations in the data
        self.no_duplicates = frame.no_duplicates # If True, no duplicate rows in the data
        self.i_t_unique = frame.i_t_unique # If True, each worker has at most one observation per period

    def _reset_attributes(self, columns_contig=True, connected=True, correct_cols=True, no_na=True, no_duplicates=True, i_t_unique=True):
        '''
        Reset class attributes conditions to be False/None.

        Arguments:
            columns_contig (bool): if True, reset self.columns_contig
            connected (bool): if True, reset self.connected
            correct_cols (bool): if True, reset self.correct_cols
            no_na (bool): if True, reset self.no_na
            no_duplicates (bool): if True, reset self.no_duplicates
            i_t_unique (bool): if True, reset self.i_t_unique

        Returns:
            self (BipartiteBase): self with reset class attributes
        '''
        if columns_contig:
            for contig_col in self.columns_contig.keys():
                if self._col_included(contig_col):
                    self.columns_contig[contig_col] = False
                else:
                    self.columns_contig[contig_col] = None
        if connected:
            self.connected = None # If False, not connected; if 'connected', all observations are in the largest connected set of firms; if 'biconnected' all observations are in the largest biconnected set of firms; if None, connectedness ignored
        if correct_cols:
            self.correct_cols = False # If True, column names are correct
        if no_na:
            self.no_na = False # If True, no NaN observations in the data
        if no_duplicates:
            self.no_duplicates = False # If True, no duplicate rows in the data
        if i_t_unique:
            self.i_t_unique = None # If True, each worker has at most one observation per period; if None, t column not included (set to False later in method if t column included)

            # Verify whether period included
            if self._col_included('t'):
                self.i_t_unique = False

        # logger_init(self)

        return self

    def _reset_id_reference_dict(self, include=False):
        '''
        Reset id_reference_dict.

        Arguments:
            include (bool): if True, id_reference_dict will track changes in ids

        Returns:
            self (BipartiteBase): self with reset id_reference_dict
        '''
        if include:
            self.id_reference_dict = {id_col: pd.DataFrame() for id_col in self.reference_dict.keys()}
        else:
            self.id_reference_dict = {}

        return self

    def _col_included(self, col):
        '''
        Check whether a column from the pre-established required/optional lists is included.

        Arguments:
            col (str): column to check. Use general column names for joint columns, e.g. put 'j' instead of 'j1', 'j2'

        Returns:
            (bool): if True, column is included
        '''
        if col in self.columns_req + self.columns_opt:
            for subcol in to_list(self.reference_dict[col]):
                if self.col_dict[subcol] is None:
                    return False
            return True
        return False

    def _included_cols(self, flat=False):
        '''
        Get all columns included from the pre-established required/optional lists.
        
        Arguments:
            flat (bool): if False, uses general column names for joint columns, e.g. returns 'j' instead of 'j1', 'j2'.

        Returns:
            all_cols (list): included columns
        '''
        all_cols = []
        for col in self.columns_req + self.columns_opt:
            include = True
            for subcol in to_list(self.reference_dict[col]):
                if self.col_dict[subcol] is None:
                    include = False
                    break
            if include:
                if flat:
                    all_cols += to_list(self.reference_dict[col])
                else:
                    all_cols.append(col)
        return all_cols

    def drop(self, indices, axis=1, inplace=True, allow_required=False):
        '''
        Drop indices along axis.

        Arguments:
            indices (int or str, optionally as a list): row(s) or column(s) to drop. For columns, use general column names for joint columns, e.g. put 'g' instead of 'g1', 'g2'. Only optional columns may be dropped
            axis (int): 0 to drop rows, 1 to drop columns
            inplace (bool): if True, modify in-place
            allow_required (bool): if True, allow to drop required columns

        Returns:
            frame (BipartiteBase): BipartiteBase with dropped indices
        '''
        if inplace:
            frame = self
        else:
            frame = self.copy()

        if axis == 1:
            for col in to_list(indices):
                if col in frame.columns or col in frame.columns_req or col in frame.columns_opt:
                    if col in frame.columns_opt: # If column optional
                        for subcol in to_list(frame.reference_dict[col]):
                            DataFrame.drop(frame, subcol, axis=1, inplace=True)
                            frame.col_dict[subcol] = None
                        if col in frame.columns_contig.keys(): # If column contiguous
                            frame.columns_contig[col] = None
                            if frame.id_reference_dict: # If id_reference_dict has been initialized
                                frame.id_reference_dict[col] = pd.DataFrame()
                    elif col not in frame._included_cols() and col not in frame._included_cols(flat=True): # If column is not pre-established
                        DataFrame.drop(frame, col, axis=1, inplace=True)
                    else:
                        if not allow_required:
                            warnings.warn("{} is either (a) a required column and cannot be dropped or (b) a subcolumn that can be dropped, but only by specifying the general column name (e.g. use 'g' instead of 'g1' or 'g2')".format(col))
                        else:
                            DataFrame.drop(frame, col, axis=1, inplace=True)
                else:
                    warnings.warn('{} is not in data columns'.format(col))
        elif axis == 0:
            DataFrame.drop(frame, indices, axis=0, inplace=True)
            frame._reset_attributes()
            frame.clean_data({'connectedness': frame.connected})

        return frame

    def rename(self, rename_dict, inplace=True):
        '''
        Rename a column.

        Arguments:
            rename_dict (dict): key is current column name, value is new column name. Use general column names for joint columns, e.g. put 'g' instead of 'g1', 'g2'. Only optional columns may be renamed
            inplace (bool): if True, modify in-place

        Returns:
            frame (BipartiteBase): BipartiteBase with renamed columns
        '''
        if inplace:
            frame = self
        else:
            frame = self.copy()

        for col_cur, col_new in rename_dict.items():
            if col_cur in frame.columns or col_cur in frame.columns_req or col_cur in frame.columns_opt:
                if col_cur in self.columns_opt: # If column optional
                    if len(to_list(self.reference_dict[col_cur])) > 1:
                        for i, subcol in enumerate(to_list(self.reference_dict[col_cur])):
                            DataFrame.rename(frame, {subcol: col_new + str(i + 1)}, axis=1, inplace=True)
                            frame.col_dict[subcol] = None
                    else:
                        DataFrame.rename(frame, {col_cur: col_new}, axis=1, inplace=True)
                        frame.col_dict[col_cur] = None
                    if col_cur in frame.columns_contig.keys(): # If column contiguous
                            frame.columns_contig[col_cur] = None
                            if frame.id_reference_dict: # If id_reference_dict has been initialized
                                frame.id_reference_dict[col_cur] = pd.DataFrame()
                elif col_cur not in frame._included_cols() and col_cur not in frame._included_cols(flat=True): # If column is not pre-established
                        DataFrame.rename(frame, {col_cur: col_new}, axis=1, inplace=True)
                else:
                    warnings.warn("{} is either (a) a required column and cannot be renamed or (b) a subcolumn that can be renamed, but only by specifying the general column name (e.g. use 'g' instead of 'g1' or 'g2')".format(col_cur))
            else:
                warnings.warn('{} is not in data columns'.format(col_cur))

        return frame

    def merge(self, *args, **kwargs):
        '''
        Merge two BipartiteBase objects.

        Arguments:
            *args: arguments for Pandas merge
            **kwargs: keyword arguments for Pandas merge

        Returns:
            frame (BipartiteBase): merged dataframe
        '''
        frame = DataFrame.merge(self, *args, **kwargs)
        frame = self._constructor(frame) # Use correct constructor
        if kwargs['how'] == 'left': # Non-left merge could cause issues with data, by default resets attributes
            frame._set_attributes(self)
        return frame

    def _check_contiguous_ids(self):
        '''
        Check whether each id column is contiguous.
        '''
        for contig_col, is_contig in self.columns_contig.items():
            if self._col_included(contig_col):
                id_max = - np.inf
                ids_unique = []
                for id_col in to_list(self.reference_dict[contig_col]):
                    id_max = max(self[id_col].max(), id_max)
                    ids_unique = list(self[id_col].unique()) + ids_unique
                n_ids = len(set(ids_unique))

                contig_ids = (id_max == n_ids - 1)
                self.columns_contig[contig_col] = contig_ids

    def _contiguous_ids(self, id_col, copy=True):
        '''
        Make column of ids contiguous.

        Arguments:
            id_col (str): column to make contiguous ('i', 'j', or 'g'). Use general column names for joint columns, e.g. put 'j' instead of 'j1', 'j2'. Only optional columns may be renamed
            copy (bool): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase with contiguous ids
        '''
        if copy:
            frame = self.copy()
        else:
            frame = self

        cols = to_list(self.reference_dict[id_col])
        n_cols = len(cols)
        n_rows = len(frame)
        all_ids = frame[cols].to_numpy().reshape(n_cols * n_rows)
        # Source: https://stackoverflow.com/questions/16453465/multi-column-factorize-in-pandas
        factorized = pd.factorize(all_ids)

        # Quickly check whether ids need to be reset
        try:
            if max(factorized[1]) + 1 == len(factorized[1]):
                return frame
        except TypeError:
            # If ids are not integers, this will return a TypeError and we can ignore it
            pass
        
        frame[cols] = factorized[0].reshape((n_rows, n_cols))

        # Save id reference dataframe, so user can revert back to original ids
        if frame.id_reference_dict: # If id_reference_dict has been initialized
            if len(frame.id_reference_dict[id_col]) == 0: # If dataframe empty, start with original ids: adjusted ids
                frame.id_reference_dict[id_col]['original_ids'] = factorized[1]
                frame.id_reference_dict[id_col]['adjusted_ids_1'] = np.arange(len(factorized[1]))
            else: # Merge in new adjustment step
                n_cols_id = len(frame.id_reference_dict[id_col].columns)
                id_reference_df = pd.DataFrame({'adjusted_ids_' + str(n_cols_id - 1): factorized[1], 'adjusted_ids_' + str(n_cols_id): np.arange(len(factorized[1]))}, index=np.arange(len(factorized[1]))).astype('Int64')
                frame.id_reference_dict[id_col] = frame.id_reference_dict[id_col].merge(id_reference_df, how='left', on='adjusted_ids_' + str(n_cols_id - 1))

        # Sort columns
        sorted_cols = sorted(frame.columns, key=col_order)
        frame = frame.reindex(sorted_cols, axis=1, copy=False)

        # ids are now contiguous
        frame.columns_contig[id_col] = True

        return frame

        # # Create sorted set of unique ids
        # ids = []
        # for id in to_list(self.reference_dict[id_col]):
        #     ids += list(frame[id].unique())
        # ids = sorted(list(set(ids)))

        # # Quickly check whether ids need to be reset
        # try:
        #     if ids[-1] + 1 == len(ids): # Recall ids is sorted
        #         return frame
        # except TypeError:
        #     # If ids are not integers, this will return a TypeError and we can ignore it
        #     pass

        # # Create list of adjusted ids
        # adjusted_ids = np.arange(len(ids)).astype(int)

        # # Save id reference dataframe, so user can revert back to original ids
        # if frame.id_reference_dict: # If id_reference_dict has been initialized
        #     if len(frame.id_reference_dict[id_col]) == 0: # If dataframe empty, start with original ids: adjusted ids
        #         frame.id_reference_dict[id_col]['original_ids'] = ids
        #         frame.id_reference_dict[id_col]['adjusted_ids_1'] = adjusted_ids
        #     else: # Merge in new adjustment step
        #         n_cols = len(frame.id_reference_dict[id_col].columns)
        #         id_reference_df = pd.DataFrame({'adjusted_ids_' + str(n_cols - 1): ids, 'adjusted_ids_' + str(n_cols): adjusted_ids}, index=adjusted_ids).astype('Int64')
        #         frame.id_reference_dict[id_col] = frame.id_reference_dict[id_col].merge(id_reference_df, how='left', on='adjusted_ids_' + str(n_cols - 1))

        # # Update each fid one at a time
        # ids_dict = dict(zip(ids, adjusted_ids))
        # for id in to_list(self.reference_dict[id_col]):
        #     # Source: https://stackoverflow.com/questions/20250771/remap-values-in-pandas-column-with-a-dict
        #     frame[id] = frame[id].map(ids_dict)

        #     # # Create dictionary linking current to new ids, then convert into a dataframe for merging
        #     # ids_dict = {id: ids, 'adj_' + id: adjusted_ids}
        #     # ids_df = pd.DataFrame(ids_dict, index=adjusted_ids)

        #     # # Merge new, contiguous ids into event study data
        #     # frame = frame.merge(ids_df, how='left', on=id, copy=False)

        #     # # Adjust id column to use new contiguous id
        #     # frame[id] = frame['adj_' + id]
        #     # frame.drop('adj_' + id)

        # # Sort columns
        # sorted_cols = sorted(frame.columns, key=col_order)
        # frame = frame.reindex(sorted_cols, axis=1, copy=False)

        # # ids are now contiguous
        # frame.columns_contig[id_col] = True

        # return frame

    def _update_cols(self, inplace=True):
        '''
        Rename columns and keep only relevant columns.

        Arguments:
            inplace (bool): if True, modify in-place

        Returns:
            frame (BipartiteBase): BipartiteBase with updated columns
        '''
        if inplace:
            frame = self
        else:
            frame = self.copy()

        new_col_dict = {}
        rename_dict = {} # For renaming columns in data
        keep_cols = []

        for key, val in frame.col_dict.items():
            if val is not None:
                rename_dict[val] = key
                new_col_dict[key] = key
                keep_cols.append(key)
            else:
                new_col_dict[key] = None
        frame.col_dict = new_col_dict
        keep_cols = sorted(keep_cols, key=col_order) # Sort columns
        DataFrame.rename(frame, rename_dict, axis=1, inplace=True)
        for col in frame.columns:
            if col not in keep_cols:
                frame.drop(col)

        return frame

    def clean_data(self, user_clean={}):
        '''
        Clean data to make sure there are no NaN or duplicate observations, firms are connected by movers and firm ids are contiguous.

        Arguments:
            user_clean (dict): dictionary of parameters for cleaning

                Dictionary parameters:

                    connectedness (str or None, default='connected'): if 'connected', keep observations in the largest connected set of firms; if 'biconnected', keep observations in the largest biconnected set of firms; if None, keep all observations

                    i_t_how (str, default='max'): if 'max', keep max paying job; if 'sum', sum over duplicate worker-firm-year observations, then take the highest paying worker-firm sum; if 'mean', average over duplicate worker-firm-year observations, then take the highest paying worker-firm average. Note that if multiple time and/or firm columns are included (as in event study format), then data is converted to long, cleaned, then reconverted to its original format

                    drop_multiples (bool): if True, rather than collapsing over spells, drop any spells with multiple observations (this is for computational efficiency when re-collapsing data for biconnected components)

                    data_validity (bool, default=True): if True, run data validity checks; much faster if set to False

                    copy (bool, default=False): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase with cleaned data
        '''
        self.logger.info('beginning BipartiteBase data cleaning')

        clean_params = update_dict(self.default_clean, user_clean)

        if clean_params['copy']:
            frame = self.copy()
        else:
            frame = self

        # # If not running _data_validity(), reset all attributes
        # if not clean_params['data_validity']:
        #     frame._reset_attributes()

        # First, correct columns
        # Note this must be done before _data_validity(), otherwise certain checks are not guaranteed to work
        frame.logger.info('correcting columns')
        frame._update_cols()

        # FIXME I believe this was necessary for an old version of gen_m(), so I commented it out to speed up the code
        # # Next, sort rows
        # frame.logger.info('sorting rows')
        # frame.sort_values(['i'] + to_list(self.reference_dict['t']), inplace=True)

        # Next, make sure data is valid - computes correct_cols, no_na, no_duplicates, connected, and contiguous, along with other checks
        if clean_params['data_validity']:
            frame.logger.info('checking quality of data')
            frame = BipartiteBase._data_validity(frame, connectedness=clean_params['connectedness']) # Shared _data_validity

        # Next, drop NaN observations
        if not frame.no_na:
            frame.logger.info('dropping NaN observations')
            frame = frame.dropna()

            # Update no_na
            frame.no_na = True

        # Next, make sure i-t (worker-year) observations are unique
        if frame.i_t_unique is not None and not frame.i_t_unique:
            frame.logger.info('keeping highest paying job for i-t (worker-year) duplicates')
            frame = frame._drop_i_t_duplicates(how=clean_params['i_t_how'], copy=False)

            # Update no_duplicates
            frame.no_duplicates = True
        elif not frame.no_duplicates:
            # Drop duplicate observations
            frame.logger.info('dropping duplicate observations')
            frame.drop_duplicates(inplace=True)

            # Update no_duplicates
            frame.no_duplicates = True

        # Next, find largest set of firms connected by movers
        if frame.connected in [False, None]:
            # Generate largest connected set
            frame.logger.info('generating largest connected set')
            frame = frame._conset(connectedness=clean_params['connectedness'], drop_multiples=clean_params['drop_multiples'], copy=False)

        # Next, check contiguous ids
        for contig_col, is_contig in frame.columns_contig.items():
            if is_contig is not None and not is_contig:
                frame.logger.info('making {} ids contiguous'.format(contig_col))
                frame = frame._contiguous_ids(id_col=contig_col, copy=False)

        # Sort columns
        frame.logger.info('sorting columns')
        sorted_cols = sorted(frame.columns, key=col_order)
        frame = frame.reindex(sorted_cols, axis=1, copy=False)

        # Reset index
        frame.reset_index(drop=True, inplace=True)

        frame.logger.info('BipartiteBase data cleaning complete')

        return frame

    def _data_validity(self, connectedness='connected'):
        '''
        Checks that data is formatted correctly and updates relevant attributes.

        Arguments:
            connectedness (str or None): if 'connected', check that observations are in the largest connected set of firms; if 'biconnected', check that observations are in the largest biconnected set of firms; if None, keep all observations

        Returns:
            frame (BipartiteBase): BipartiteBase with corrected attributes
        '''
        frame = self # .copy()

        success = True

        frame.logger.info('--- checking columns ---')
        all_cols = frame._included_cols()
        cols = True
        frame.logger.info('--- checking column datatypes ---')
        col_dtypes = True
        for col in all_cols:
            for subcol in to_list(frame.reference_dict[col]):
                if frame.col_dict[subcol] not in frame.columns:
                    frame.logger.info('{} missing from data'.format(frame.col_dict[subcol]))
                    col_dtypes = False
                    cols = False
                else:
                    col_type = str(frame[frame.col_dict[subcol]].dtype)
                    valid_types = to_list(frame.dtype_dict[frame.col_dtype_dict[col]])
                    if col_type not in valid_types:
                        frame.logger.info('{} has wrong dtype, should be {} but is {}'.format(frame.col_dict[subcol], frame.col_dtype_dict[col], col_type))
                        if col in frame.columns_contig.keys(): # If column contiguous
                            frame.logger.info('{} has wrong dtype, converting to contiguous integers'.format(frame.col_dict[subcol]))
                            frame = frame._contiguous_ids(col)
                        else:
                            frame.logger.info('{} has wrong dtype. Please check that this is the correct column (it is supposed to give {}), and if it is, cast it to a valid datatype (these include: {})'.format(frame.col_dict[subcol], subcol, valid_types))
                            col_dtypes = False
                            cols = False

        frame.logger.info('column datatypes correct:' + str(col_dtypes))
        if not col_dtypes:
            success = False
            raise ValueError('Your data does not include the correct columns or column datatypes. The BipartitePandas object cannot be generated with your data.')

        frame.logger.info('--- checking column names ---')
        col_names = True
        for col in all_cols:
            for subcol in to_list(frame.reference_dict[col]):
                if frame.col_dict[subcol] != subcol:
                    col_names = False
                    cols = False
                    break

        frame.logger.info('column names correct:' + str(col_names))
        if not col_names:
            success = False

        frame.logger.info('--- checking non-pre-established columns ---')
        all_cols = frame._included_cols(flat=True)
        for col in frame.columns:
            if col not in all_cols:
                cols = False
                break

        frame.logger.info('columns correct:' + str(cols))
        if not cols:
            frame.correct_cols = False
        else:
            frame.correct_cols = True

        frame.logger.info('--- checking nan data ---')
        nans = frame.shape[0] - frame.dropna().shape[0]

        frame.logger.info('data nans (should be 0):' + str(nans))
        if nans > 0:
            frame.no_na = False
            success = False
        else:
            frame.no_na = True

        frame.logger.info('--- checking duplicates ---')
        duplicates = frame.shape[0] - frame.drop_duplicates().shape[0]

        frame.logger.info('duplicates (should be 0):' + str(duplicates))
        if duplicates > 0:
            frame.no_duplicates = False
            success = False
        else:
            frame.no_duplicates = True

        if frame._col_included('t'):
            frame.logger.info('--- checking i-t (worker-year) observations ---')
            max_obs = 1
            for t_col in to_list(frame.reference_dict['t']):
                max_obs_col = frame.groupby(['i', t_col]).size().max()
                max_obs = max(max_obs_col, max_obs)

            frame.logger.info('max number of i-t (worker-year) observations (should be 1):' + str(max_obs))
            if max_obs > 1:
                frame.i_t_unique = False
                success = False
            else:
                frame.i_t_unique = True
        else:
            frame.i_t_unique = None

        if connectedness is None:
            # Skipping connected set
            self.connected = None
        else:
            frame.logger.info('--- checking connected set ---')
            # Create graph
            if len(to_list(frame.reference_dict['j'])) == 1:
                j_first = frame.groupby(['i'])['j'].transform('first')
                G = nx.from_edgelist(pd._libs.lib.fast_zip([frame['j'].to_numpy(), j_first.to_numpy()])) # nx.from_pandas_edgelist(frame, 'j', 'j_max')
                # # Drop fid_max
                # frame.drop('j_max', axis=1)
            elif len(to_list(frame.reference_dict['j'])) == 2:
                G = nx.from_edgelist(pd._libs.lib.fast_zip([frame['j1'].to_numpy(), frame['j2'].to_numpy()])) # nx.from_pandas_edgelist(frame, 'j1', 'j2')
            else:
                warnings.warn("Trying to create network with 3 or more edges is not possible. Please check df.reference_dict['j']")
            # Find largest connected set of firms
            connectedness_dict = {
                'connected': nx.is_connected,
                'biconnected': nx.is_biconnected
            }
            is_connected = connectedness_dict[connectedness](G)

            frame.logger.info('data is {}: {}'.format(connectedness, frame.connected))
            if not is_connected:
                frame.connected = False
                success = False
            else:
                frame.connected = connectedness

        # Check contiguous columns
        for contig_col, is_contig in frame.columns_contig.items():
            if frame._col_included(contig_col):
                frame.logger.info('--- checking contiguous {} ids ---'.format(contig_col))
                id_max = - np.inf
                ids_unique = []
                for id_col in to_list(frame.reference_dict[contig_col]):
                    id_max = max(frame[id_col].max(), id_max)
                    ids_unique = list(frame[id_col].unique()) + ids_unique
                n_ids = len(set(ids_unique))

                contig_ids = (id_max == n_ids - 1)
                frame.columns_contig[contig_col] = contig_ids

                frame.logger.info('contiguous {} ids (should be True): {}'.format(contig_col, contig_ids))
                if not contig_ids:
                    success = False
            else:
                frame.logger.info('--- skipping contiguous {} ids, column(s) not included ---'.format(contig_col))

        frame.logger.info('BipartiteBase success:' + str(success))

        return frame

    def _drop_i_t_duplicates(self, how='max', copy=True):
        '''
        Keep only the highest paying job for i-t (worker-year) duplicates.

        Arguments:
            how (str): if 'max', keep max paying job; if 'sum', sum over duplicate worker-firm-year observations, then take the highest paying worker-firm sum; if 'mean', average over duplicate worker-firm-year observations, then take the highest paying worker-firm average. Note that if multiple time and/or firm columns are included (as in event study format), then duplicates are cleaned in order of earlier time columns to later time columns, and earlier firm ids to later firm ids
            copy (bool): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase that keeps only the highest paying job for i-t (worker-year) duplicates. If no t column(s), returns frame with no changes
        '''
        if copy:
            frame = self.copy()
        else:
            frame = self

        if frame._col_included('t'):
            try: # If BipartiteEventStudy or BipartiteEventStudyCollapsed
                frame = frame.unstack_es().drop('m').drop_duplicates()
                convert_1 = True
            except AttributeError:
                convert_1 = False
            try: # If BipartiteLongCollapsed
                frame = frame.uncollapse()
                convert_2 = True
            except AttributeError:
                convert_2 = False

            if how == 'max':
                # Source: https://stackoverflow.com/questions/23394476/keep-other-columns-when-doing-groupby
                frame = frame[frame['y'] == frame.groupby(['i', 't'])['y'].transform(max)].groupby(['i', 't'], as_index=False).first()
                # frame.sort_values('y').groupby(['i', 't'], as_index=False).last()
                # frame = frame.iloc[frame.reset_index().groupby(['i', 't']).agg({'y': max, 'index': 'first'})['index']].reset_index(drop=True)
                # # Sort by worker id, time, and compensation
                # frame.sort_values(['i', 't', 'y'], inplace=True)
                # frame.drop_duplicates(subset=['i', 't'], keep='last', inplace=True)
            elif how in ['sum', 'mean']:
                # Group by worker id, time, and firm id, and take sum/mean of compensation
                frame['y'] = frame.groupby(['i', 't', 'j'])['y'].transform(how)
                frame = frame[frame['y'] == frame.groupby(['i', 't'])['y'].transform(max)].groupby(['i', 't'], as_index=False).first()
                # frame = frame.iloc[frame.reset_index().groupby(['i', 't']).agg({'y': max, 'index': 'first'})['index']].reset_index(drop=True)
                # # Sort by worker id, time, and compensation
                # frame.sort_values(['i', 't', 'y'], inplace=True)
                # # For each i-t group, take max compensation
                # frame.drop_duplicates(subset=['i', 't'], keep='last', inplace=True)
            else:
                warnings.warn('{} is not a valid method for dropping i-t duplicates'.format(how))

        # Data now has unique i-t observations
        frame.i_t_unique = True

        if convert_2: # If data was collapsed
            frame = frame.get_collapsed_long(copy=copy).drop('m')
        if convert_1: # If data was event study
            frame = frame.get_es()

        return frame

    def _conset(self, connectedness='connected', drop_multiples=False, copy=True):
        '''
        Update data to include only the largest connected set of movers, and if firm ids are contiguous, also return the NetworkX Graph.

        Arguments:
            connectedness (str or None): if 'connected', keep observations in the largest connected set of firms; if 'biconnected', keep observations in the largest biconnected set of firms; if None, keep all observations
            drop_multiples (bool): if True, rather than collapsing over spells, drop any spells with multiple observations (this is for computational efficiency when re-collapsing data for biconnected components)
            copy (bool): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase with connected set of movers
            ALTERNATIVELY
            (tuple):
                frame (BipartiteBase): BipartiteBase with connected set of movers
                G (NetworkX Graph): largest connected set of movers (only returns if firm ids are contiguous, otherwise returns None)
        '''
        if copy:
            frame = self.copy()
        else:
            frame = self

        if connectedness is None:
            # Skipping connected set
            frame.connected = None
            # frame._check_contiguous_ids() # This is necessary
            return frame

        prev_workers = frame.n_workers()
        prev_firms = frame.n_firms()
        prev_clusters = frame.n_clusters()
        # Create graph
        if len(to_list(frame.reference_dict['j'])) == 1:
            # Add max firm id per worker to serve as a central node for the worker
            # frame['fid_f1'] = frame.groupby('wid')['fid'].transform(lambda a: a.shift(-1)) # FIXME - this is directed but is much slower
            j_first = frame.groupby('i')['j'].transform('first') # FIXME - this is undirected but is much faster

            # Find largest connected set (look only at movers)
            # Source: https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.connected_components.html
            # Source for values.tolist(): https://stackoverflow.com/questions/44849668/merge-two-columns-in-pandas-dataframe-into-a-list
            # Source for fast_zip: https://stackoverflow.com/questions/16453465/multi-column-factorize-in-pandas
            G = nx.from_edgelist(pd._libs.lib.fast_zip([frame['j'].to_numpy(), j_first.to_numpy()])) # nx.from_edgelist(frame[['j', 'j_first']].to_numpy().tolist()) # nx.from_pandas_edgelist(frame[['j', 'j_first']], 'j', 'j_first')
            # # Drop j_first
            # frame.drop('j_first')
            del j_first
        elif len(to_list(frame.reference_dict['j'])) == 2:
            G = nx.from_edgelist(pd._libs.lib.fast_zip([frame['j1'].to_numpy(), frame['j2'].to_numpy()])) # nx.from_edgelist(frame[['j1', 'j2']].to_numpy().tolist()) # nx.from_pandas_edgelist(frame[['j1', 'j2']], 'j1', 'j2')
        else:
            warnings.warn("Trying to create network with 3 or more edges is not possible. Please check df.reference_dict['j'].")

        # Update data
        # Find largest connected set of firms
        if connectedness == 'connected':
            largest_cc = max(nx.connected_components(G), key=len)
        elif connectedness == 'biconnected':
            if isinstance(frame, bpd.BipartiteEventStudyCollapsed):
                raise NotImplementedError('Cannot compute biconnected components on collapsed event study data. This is because intermediate firms can be dropped, turning a mover into a stayer - for instance, a worker may work at firms A, B, then return to A. But if B is not in the largest biconnected set of firms, the worker now has their associated firms listed as A, A. These observations should be collapsed into a single observation, but there is not currently a way to collapse this data efficiently if it is formatted as a collapsed event study. Please compute biconnected components on another data format.')
            largest_cc = max(nx.biconnected_components(G), key=len)
        else:
            warnings.warn("Invalid connectedness: {}. Valid options are 'connected', 'biconnected', or None.".format(connectedness))
        # Keep largest connected set of firms
        if len(to_list(frame.reference_dict['j'])) == 1:
            frame = frame[frame['j'].isin(largest_cc)]
            if isinstance(frame, bpd.BipartiteLongCollapsed): # and (connectedness == 'biconnected'):
                frame = frame.recollapse(drop_multiples=drop_multiples, copy=False)
        else:
            frame = frame[(frame['j1'].isin(largest_cc)) & (frame['j2'].isin(largest_cc))]

        # Data is now connected
        frame.connected = connectedness

        # If connected data != full data, set contiguous to False
        if prev_workers != frame.n_workers():
            frame.columns_contig['i'] = False
        if prev_firms != frame.n_firms():
            frame.columns_contig['j'] = False
        if prev_clusters is not None and prev_clusters != frame.n_clusters():
            frame.columns_contig['g'] = False

        return frame

    def gen_m(self, inplace=True):
        '''
        Generate m column for data (m == 0 if stayer, m == 1 if mover).

        Arguments:
            inplace (bool): if True, modify in-place

        Returns:
            frame (BipartiteBase): BipartiteBase with m column
        '''
        if inplace:
            frame = self
        else:
            frame = self.copy()

        if not frame._col_included('m'):
            if len(to_list(frame.reference_dict['j'])) == 1:
                frame['m'] = (frame.groupby('i')['j'].transform('nunique') > 1).astype(int) # (aggregate_transform(frame, col_groupby='i', col_grouped='j', func='n_unique', col_name='m') > 1).astype(int)
            elif len(to_list(frame.reference_dict['j'])) == 2:
                frame['m'] = (frame['j1'] != frame['j2']).astype(int)
                # frame['m'] = frame.groupby('i')['m'].transform('max')
            else:
                warnings.warn("Trying to compute whether an individual moved firms is not possible with 3 or more firms per observation. Please check df.reference_dict['j']. Returning unaltered frame")
                return frame
            frame.col_dict['m'] = 'm'
            # Sort columns
            sorted_cols = sorted(frame.columns, key=col_order)
            frame = frame.reindex(sorted_cols, axis=1, copy=False)
        else:
            self.logger.info('m column already included. Returning unaltered frame')

        return frame

    def keep_ids(self, id_col, keep_ids, copy=True):
        '''
        Only keep ids belonging to a given set of ids.

        Arguments:
            id_col (str): column of ids to consider ('i', 'j', or 'g')
            keep_ids (list): ids to keep
            copy (bool): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase with ids in the given set
        '''
        if copy:
            frame = self.copy()
        else:
            frame = self

        for id_subcol in to_list(self.reference_dict[id_col]):
            frame = frame[frame[id_subcol].isin(keep_ids)]

        frame.reset_index(drop=True, inplace=True)

        return frame

    def drop_ids(self, id_col, drop_ids, copy=True):
        '''
        Drop all ids belonging to a given set of ids.

        Arguments:
            id_col (str): column of ids to consider ('i', 'j', or 'g')
            drop_ids (list): ids to drop
            copy (bool): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase with ids in the given set
        '''
        if copy:
            frame = self.copy()
        else:
            frame = self

        for id_subcol in to_list(self.reference_dict[id_col]):
            frame = frame[~(frame[id_subcol].isin(drop_ids))]

        frame.reset_index(drop=True, inplace=True)

        return frame

    def min_movers(self, threshold=15, copy=True):
        '''
        List firms with at least `threshold` many movers.

        Arguments:
            threshold (int): minimum number of movers required to keep a firm
            copy (bool): if False, avoid copy

        Returns:
            valid_firms (list): list of firms with sufficiently many movers
        '''
        # Generate m column (the function checks if it already exists)
        self.gen_m()

        if copy:
            frame = self.copy()
        else:
            frame = self

        frame = frame[frame['m'] == 1] # Keep movers

        j_cols = to_list(self.reference_dict['j'])
        n_movers = frame.groupby(j_cols[0])['i'].unique().apply(list) # List of all unique worker ids for j/j1
        # Convert into DataFrame for merging
        n_movers = pd.DataFrame(n_movers)
        n_movers.reset_index(inplace=True)
        n_movers.rename({j_cols[0]: 'j'}, axis=1, inplace=True)

        for j_col in j_cols[1:]:
            n_movers_merge = frame.groupby(j_col)['i'].unique().apply(list)
            # Convert into DataFrame for merging
            n_movers_merge = pd.DataFrame(n_movers_merge)
            n_movers_merge.reset_index(inplace=True)
            n_movers_merge.rename({j_col: 'j'}, axis=1, inplace=True)
            # Merge
            n_movers = pd.merge(n_movers, n_movers_merge, on='j')
            # Correct columns
            n_movers[['i_x', 'i_y']] = n_movers[['i_x', 'i_y']].fillna('').apply(list) # Replace NaNs with empty list, source: https://stackoverflow.com/questions/33199193/how-to-fill-dataframe-nan-values-with-empty-list-in-pandas
            n_movers['i'] = n_movers['i_x'] + n_movers['i_y'] # Total movers
            n_movers = n_movers[['j', 'i']]

        # Get number of unique movers at firm j
        n_movers['i'] = n_movers['i'].apply(set).apply(len)
        valid_firms = n_movers.loc[n_movers['i'] >= threshold, 'j']

        return valid_firms

    def _prep_cluster_data(self, stayers_movers=None, t=None, weighted=True):
        '''
        Prepare data for clustering.

        Arguments:
            stayers_movers (str or None, default=None): if None, clusters on entire dataset; if 'stayers', clusters on only stayers; if 'movers', clusters on only movers
            t (int or None, default=None): if None, clusters on entire dataset; if int, gives period in data to consider (only valid for non-collapsed data)
            weighted (bool, default=True): if True, weight firm clusters by firm size (if a weight column is included, firm weight is computed using this column; otherwise, each observation has weight 1)
        Returns:
            data (Pandas DataFrame): data prepared for clustering
            weights (NumPy Array or None): if weighted=True, gives NumPy array of firm weights for clustering; otherwise, is None
            jids (NumPy Array): firm ids of firms in subset of data used to cluster
        '''
        # Prepare data
        if stayers_movers is not None: # Note this condition is split into two sections, one prior to stacking event study data and one post
            # Generate m column (the function checks if it already exists)
            self.gen_m()

        # Stack data if event study (need all data in 1 column)
        try:
            frame = self.get_long(return_df=True) # Returns Pandas dataframe, not BipartiteLong(Collapsed)
        except AttributeError:
            frame = self

        if stayers_movers is not None:
            if stayers_movers == 'stayers':
                data = pd.DataFrame(frame[frame['m'] == 0])
            elif stayers_movers == 'movers':
                data = pd.DataFrame(frame[frame['m'] == 1])
        else:
            data = pd.DataFrame(frame)

        # If period-level, then only use data for that particular period
        if t is not None:
            if len(to_list(self.reference_dict['t'])) == 1:
                data = data[data['t'] == t]
            else:
                warnings.warn('Cannot use data from a particular period on collapsed data, proceeding to cluster on all data')

        # Create weights
        if weighted:
            if self._col_included('w'):
                data['row_weights'] = data['w']
                weights = data.groupby('j')['w'].sum().to_numpy()
            else:
                data['row_weights'] = 1
                weights = data.groupby('j').size().to_numpy()
        else:
            data['row_weights'] = 1
            weights = None

        # Get unique firm ids
        jids = sorted(data['j'].unique()) # Must sort

        return data, weights, jids

    def cluster(self, measures=bpd.measures.cdfs(), grouping=bpd.grouping.kmeans(), stayers_movers=None, t=None, weighted=True, dropna=False, copy=False):
        '''
        Cluster data and assign a new column giving the cluster for each firm.

        Arguments:
            measures (function or list of functions): how to compute measures for clustering. Options can be seen in bipartitepandas.measures.
            grouping (function): how to group firms based on measures. Options can be seen in bipartitepandas.grouping.
            stayers_movers (str or None): if None, clusters on entire dataset; if 'stayers', clusters on only stayers; if 'movers', clusters on only movers
            t (int or None): if None, clusters on entire dataset; if int, gives period in data to consider (only valid for non-collapsed data)
            weighted (bool): if True, weight firm clusters by firm size (if a weight column is included, firm weight is computed using this column; otherwise, each observation has weight 1)
            dropna (bool): if True, drop observations where firms aren't clustered; if False, keep all observations
            copy (bool): if False, avoid copy

        Returns:
            frame (BipartiteBase): BipartiteBase with clusters
        '''
        if copy:
            frame = self.copy()
        else:
            frame = self

        # Prepare data for clustering
        cluster_data, weights, jids = self._prep_cluster_data(stayers_movers=stayers_movers, t=t, weighted=weighted)

        # Compute measures
        for i, measure in enumerate(to_list(measures)):
            if i == 0:
                computed_measures = measure(cluster_data, jids)
            else:
                # For computing both cdfs and moments
                computed_measures = np.concatenate([computed_measures, measure(cluster_data, jids)], axis=1)
        frame.logger.info('firm moments computed')

        # Can't group using quantiles if more than 1 column
        if (grouping.__name__ == 'compute_quantiles') and (computed_measures.shape[1] > 1):
            grouping = bpd.measures.kmeans()
            warnings.warn('Cannot cluster using quantiles if multiple measures computed. Defaulting to KMeans.')

        # Compute firm groups
        frame.logger.info('computing firm groups')
        clusters = grouping(computed_measures, weights)
        frame.logger.info('firm groups computed')

        # Drop columns (because prepared data is not always a copy, must drop from self)
        for col in ['row_weights', 'one']:
            if col in self.columns:
                self.drop(col)

        # Drop existing clusters
        if frame._col_included('g'):
            frame.drop('g')

        for i, j_col in enumerate(to_list(frame.reference_dict['j'])):
            if len(to_list(self.reference_dict['j'])) == 1:
                g_col = 'g'
            elif len(to_list(self.reference_dict['j'])) == 2:
                g_col = 'g' + str(i + 1)
            clusters_dict = {j_col: jids, g_col: clusters}
            clusters_df = pd.DataFrame(clusters_dict, index=np.arange(len(jids)))
            frame.logger.info('dataframe linking fids to clusters generated')

            # Merge into event study data
            frame = frame.merge(clusters_df, how='left', on=j_col, copy=False)
            # Keep column as int even with nans
            frame[g_col] = frame[g_col].astype('Int64')
            frame.col_dict[g_col] = g_col

        # Sort columns
        sorted_cols = sorted(frame.columns, key=col_order)
        frame = frame.reindex(sorted_cols, axis=1, copy=False)

        if dropna:
            # Drop firms that don't get clustered
            frame.dropna(inplace=True)
            frame.reset_index(drop=True, inplace=True)
            frame[frame.reference_dict['g']] = frame[frame.reference_dict['g']].astype(int)
            frame.clean_data({'connectedness': frame.connected}) # Compute same connectedness measure

        frame.columns_contig['g'] = True

        frame.logger.info('clusters merged into data')

        return frame
