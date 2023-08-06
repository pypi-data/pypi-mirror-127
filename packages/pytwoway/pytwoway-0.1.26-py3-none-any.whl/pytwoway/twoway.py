'''
Class for a two-way fixed effect network
'''
import warnings
import bipartitepandas as bpd
import pytwoway as tw

class TwoWay():
    '''
    Class of TwoWay, where TwoWay gives a network of firms and workers.
    '''

    def __init__(self, data, formatting='long', col_dict=None):
        '''
        Arguments:
            data (Pandas DataFrame): data giving firms, workers, and compensation
            formatting (str): if 'long', then data in long format; if 'long_collapsed' then in collapsed long format; if 'es', then data in event study format; if 'es_collapsed' then in collapsed event study format. If simulating data, keep default value of 'long'
            col_dict (dict): make data columns readable. Keep None if column names already correct. Options for:

                long: requires: i (worker id), j (firm id), y (compensation), t (period); optional: g (firm cluster), m (0 if stayer, 1 if mover)

                collapsed long: requires: i (worker id), j (firm id), y (compensation), t1 (first period in spell), t2 (last period in spell); optional: w (weight), g (firm cluster), m (0 if stayer, 1 if mover)

                event study: requires: i (worker id), j1 (firm 1 id), j2 (firm 2 id), y1 (compensation 1), y2 (compensation 2); optional: t1 (time of observation 1), t2 (time of observation 2), g1 (firm 1 cluster), g2 (firm 2 cluster), m (0 if stayer, 1 if mover)

                collapsed event study: requires: i (worker id), j1 (firm 1 id), j2 (firm 1 id), y1 (compensation 1), y2 (compensation 2); optional: t11 (first period in observation 1 spell), t12 (last period in observation 1 spell), t21 (first period in observation 2 spell), t22 (last period in observation 2 spell), w1 (weight 1), w2 (weight 2), g1 (firm 1 cluster), g2 (firm 2 cluster), m (0 if stayer, 1 if mover)
        '''
        # Start logger
        bpd.logger_init(self)
        # self.logger.info('initializing TwoWay object')

        self.type_dict = { # Determine type based on formatting
            'long': bpd.BipartiteLong,
            'long_collapsed': bpd.BipartiteLongCollapsed,
            'es': bpd.BipartiteEventStudy,
            'es_collapsed': bpd.BipartiteEventStudyCollapsed
        }

        if isinstance(data, bpd.BipartiteBase):
            self.data = data
        else:
            self.data = self.type_dict[formatting](data, col_dict=col_dict)

        self.clean = False # Whether data is clean
        self.clustered = False # Whether data is clustered

        # self.logger.info('TwoWay object initialized')

    def _clean(self, user_clean={}, he=False):
        '''
        Clean data.

        Arguments:
            user_clean (dict): dictionary of parameters for cleaning

                Dictionary parameters:

                    connectedness (str or None, default='connected'): if 'connected', keep observations in the largest connected set of firms; if 'biconnected', keep observations in the largest biconnected set of firms; if None, keep all observations

                    i_t_how (str, default='max'): if 'max', keep max paying job; if 'sum', sum over duplicate worker-firm-year observations, then take the highest paying worker-firm sum; if 'mean', average over duplicate worker-firm-year observations, then take the highest paying worker-firm average. Note that if multiple time and/or firm columns are included (as in event study format), then duplicates are cleaned in order of earlier time columns to later time columns, and earlier firm ids to later firm ids

                    data_validity (bool, default=True): if True, run data validity checks; much faster if set to False

                    copy (bool, default=False): if False, avoid copy
            he (bool): if True, compute largest biconnected set of firms for heteroskedastic correction
        '''
        if not self.clean:
            if he:
                # Must be biconnected for heteroskedastic correction
                user_clean = user_clean.copy()
                user_clean['connectedness'] = 'biconnected'
            self.data = self.data.clean_data(user_clean=user_clean)
            self.data.gen_m()
            self.clean = True

    def prep_data(self, collapsed=True, user_clean={}, he=False):
        '''
        Prepare bipartite network for running estimators.

        Arguments:
            collapsed (bool): if True, run estimators on data collapsed by worker-firm spells
            user_clean (dict): dictionary of parameters for cleaning

                Dictionary parameters:

                    connectedness (str or None, default='connected'): if 'connected', keep observations in the largest connected set of firms; if 'biconnected', keep observations in the largest biconnected set of firms; if None, keep all observations

                    i_t_how (str, default='max'): if 'max', keep max paying job; if 'sum', sum over duplicate worker-firm-year observations, then take the highest paying worker-firm sum; if 'mean', average over duplicate worker-firm-year observations, then take the highest paying worker-firm average. Note that if multiple time and/or firm columns are included (as in event study format), then duplicates are cleaned in order of earlier time columns to later time columns, and earlier firm ids to later firm ids

                    data_validity (bool, default=True): if True, run data validity checks; much faster if set to False

                    copy (bool, default=False): if False, avoid copy
            he (bool): if True, compute largest biconnected set of firms for heteroskedastic correction
        '''
        # Clean the data
        self._clean(user_clean=user_clean, he=he)
        # Collapse the data
        if collapsed:
            if isinstance(self.data, self.type_dict['es']):
                self.data = self.data.get_long()
            if isinstance(self.data, self.type_dict['long']):
                self.data = self.data.get_collapsed_long()

    def cluster(self, measures=bpd.measures.cdfs(), grouping=bpd.grouping.kmeans(), stayers_movers=None, t=None, weighted=True, dropna=False):
        '''
        Cluster data and assign a new column giving the cluster for each firm.

        Arguments:
            measures (function or list of functions): how to compute measures for clustering. Options can be seen in bipartitepandas.measures.
            grouping (function): how to group firms based on measures. Options can be seen in bipartitepandas.grouping.
            stayers_movers (str or None): if None, clusters on entire dataset; if 'stayers', clusters on only stayers; if 'movers', clusters on only movers
            t (int or None): if None, clusters on entire dataset; if int, gives period in data to consider (only valid for non-collapsed data)
            weighted (bool): if True, weight firm clusters by firm size (if a weight column is included, firm weight is computed using this column; otherwise, each observation has weight 1)
            dropna (bool): if True, drop observations where firms aren't clustered; if False, keep all observations
        '''
        self.data = self.data.cluster(measures=measures, grouping=grouping, stayers_movers=stayers_movers, t=t, weighted=weighted, dropna=dropna)
        self.clustered = True

    def fit_fe(self, user_fe={}):
        '''
        Fit the bias-corrected FE estimator. Saves two dictionary attributes: self.fe_res (complete results) and self.fe_summary (summary results).

        Arguments:
            user_fe (dict): dictionary of parameters for bias-corrected FE estimation

                Dictionary parameters:

                    ncore (int, default=1): number of cores to use

                    batch (int, default=1): batch size to send in parallel

                    ndraw_pii (int, default=50): number of draws to use in approximation for leverages

                    levfile (str, default=''): file to load precomputed leverages

                    ndraw_tr (int, default=5): number of draws to use in approximation for traces

                    he (bool, default=False): if True, compute heteroskedastic correction

                    out (str, default='res_fe.json'): outputfile where results are saved

                    statsonly (bool, default=False): if True, return only basic statistics

                    feonly (bool, default=False): if True, compute only fixed effects and not variances

                    Q (str, default='cov(alpha, psi)'): which Q matrix to consider. Options include 'cov(alpha, psi)' and 'cov(psi_t, psi_{t+1})'

                    seed (int, default=None): NumPy RandomState seed
        '''
        # Run estimator
        if isinstance(self.data, (self.type_dict['es'], self.type_dict['es_collapsed'])):
            fe_solver = tw.FEEstimator(self.data.get_long(), user_fe)
        else:
            fe_solver = tw.FEEstimator(self.data, user_fe)
        fe_solver.fit_1()
        fe_solver.construct_Q() # Comment out this line and manually create Q if you want a custom Q matrix
        fe_solver.fit_2()

        self.fe_res = fe_solver.res
        self.fe_summary = fe_solver.summary

    def fit_cre(self, user_cre={}):
        '''
        Fit the CRE estimator. Saves two dictionary attributes: self.cre_res (complete results) and self.cre_summary (summary results).

        Arguments:
            user_cre (dict): dictionary of parameters for CRE estimation

                Dictionary parameters:

                    ncore (int, default=1): number of cores to use

                    ndraw_tr (int, default=5): number of draws to use in approximation for traces

                    ndp (int, default=50): number of draw to use in approximation for leverages

                    out (str, default='res_cre.json'): outputfile where results are saved

                    posterior (bool, default=False): if True, compute posterior variance

                    wo_btw (bool, default=False): if True, sets between variation to 0, pure RE
        ''' 
        # Run estimator
        if isinstance(self.data, (self.type_dict['long'], self.type_dict['long_collapsed'])):
            cre_solver = tw.CREEstimator(self.data.get_es().get_cs(), user_cre)
        else:
            cre_solver = tw.CREEstimator(self.data.get_cs(), user_cre)
        cre_solver.fit()

        self.cre_res = cre_solver.res
        self.cre_summary = cre_solver.summary

    def summary_fe(self):
        '''
        Return summary results for FE estimator.

        Returns:
            self.fe_summary (dict): dictionary of FE summary results
        '''
        return self.fe_summary

    def summary_cre(self):
        '''
        Return summary results for CRE estimator.

        Returns:
            self.cre_summary (dict): dictionary of CRE summary results
        '''
        return self.cre_summary
