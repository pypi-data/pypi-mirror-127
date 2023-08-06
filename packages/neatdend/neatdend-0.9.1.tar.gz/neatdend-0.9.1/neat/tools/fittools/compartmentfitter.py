import numpy as np

import matplotlib.patheffects as patheffects
import matplotlib.patches as patches
import matplotlib.cm as cm
import matplotlib.pyplot as pl
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D

from ...trees.morphtree import MorphLoc
from ...trees.phystree import PhysTree
from ...trees.greenstree import GreensTree
from ...trees.sovtree import SOVTree
from ...trees.netree import NET, NETNode, Kernel

from ...tools import kernelextraction as ke

import warnings
import copy
import pickle
import concurrent.futures
import contextlib
import multiprocessing

try:
    from ...tools.simtools.neuron import neuronmodel as neurm
except ModuleNotFoundError:
    warnings.warn('NEURON not available', UserWarning)


def cpu_count(use_hyperthreading=True):
    """
    Return number of available cores.
    Makes use of hypterthreading by default.
    """
    if use_hyperthreading:
        return multiprocessing.cpu_count()
    else:
        return multiprocessing.cpu_count() // 2


def consecutive(inds):
    """
    split a list of ints into consecutive sublists
    """
    return np.split(inds, np.where(np.diff(inds) != 1)[0]+1)


def getExpansionPoints(e_hs, channel, only_e_h=False):
    """
    Returns a list of expansion points around which to compute the impedance
    matrix given a set of holding potentials. If the channel has only one state
    variable, the returned expansion points are at the holding potentials, if
    the channels has two state variables, the returned expansions points are
    are different combinations of the state variable values around the holding
    potentials

    Parameters
    ----------
    e_hs: iterable collection
        The holding potentials around which the expansion points are computed
    channel: `neat.channels.ionchannels.IonChannel`
        The ion channels
    only_e_h: bool
        If True, othe entries in ``sv_hs`` are only at ``e_hs``

    Returns
    -------
    sv_hs: list of dict
        Each entry is a state variable expansion point
    e_hs: list of float
        The holding potentials corresponding to each entry in ``sv_hs``
    """
    e_hs = list(e_hs)
    if len(channel.statevars) == 1 or only_e_h:
        sv_hs = [channel.computeVarinf(e_h) for e_h in e_hs]
    elif len(channel.statevars) == 2:
        # evaluate at the holding potentials
        sv_aux = [channel.computeVarinf(e_h) for e_h in e_hs]

        # check which variable is activation
        sv = channel.computeVarinf(np.array([-43.22, -32.22]))
        sind_act = None
        for ii, svar in enumerate(channel.ordered_statevars):
            if sv[svar][1] > sv[svar][0]:
                sind_act = 'ii' if ii == 0 else 'jj'

        # evaluate at combinations of holding potentials
        sv_hs_extra, e_hs_extra = [], []
        sv_o = channel.ordered_statevars
        for ii, sv_1 in enumerate(sv_aux):
            for jj, sv_2 in enumerate(sv_aux):
                sv_hs_extra.append({str(sv_o[0]): sv_1[sv_o[0]],
                                    str(sv_o[1]): sv_2[sv_o[1]]})
                # follow holding potential of activation state variable
                e_hs_extra.append(eval('e_hs[%s]'%sind_act))

        sv_hs = sv_aux + sv_hs_extra
        e_hs = e_hs + e_hs_extra
    else:
        raise Exception('Method only implemented for channels with two ' + \
                        'or less state variables')

    return sv_hs, e_hs


def asPassiveDendrite(phys_tree, factor_lambda=2., t_calibrate=500.):
        """
        Set the dendrites to be passive compartments. Channel conductances at
        the resting potential are added to passive membrane conductance.

        Parameters
        ----------
        phys_tree: `neat.PhysTree()`
            the neuron model
        factor_lambda: float (optional, defaults to 2.)
            multiplies the numbers of compartments given by the lambda rule (to
            compute resting membrane potential)
        t_calibrate: float (optional, defaults to 500. ms)
            The calibration time for the model (should reach resting potential)

        Returns
        -------
        `neat.PhysTree()`
        """
        dt, t_max = .1, 1.
        # create a biophysical simulation model
        sim_tree = phys_tree.__copy__(new_tree=neurm.NeuronSimTree())
        # compute equilibrium potentials
        sim_tree.initModel(dt=dt, factor_lambda=factor_lambda, t_calibrate=t_calibrate)
        sim_tree.storeLocs([(node.index, .5) for node in phys_tree], 'rec locs')
        res = sim_tree.run(t_max)
        sim_tree.deleteModel()
        v_eqs = [v_m[-1] for v_m in res['v_m']]
        # store the equilbirum potential distribution
        phys_tree.setEEq(v_eqs)
        phys_tree.asPassiveMembrane(node_arg='basal')
        phys_tree.asPassiveMembrane(node_arg='apical')
        phys_tree.setCompTree(eps=1e-2)

        return phys_tree


class FitTreeGF(GreensTree):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setName('dont save', '')

    def setExpansionPointsForFit(self, sv_h, e_h):
        """
        Set the holding potentials and expansion points for the fit

        Parameters
        ----------
        sv_hs: dict of {string: np.ndarray}
            Keys are the channel names and values are numpy arrays that contain
            the expansion point for each ion channel
        e_h: float
            the holding potential
        """
        for node in self:
            node.setEEq(e_h)
            for c_name, sv in sv_h.items():
                node.setExpansionPoint(c_name, statevar=sv)

    def setName(self, name, path):
        """
        Set the name and path under which the tree will be stored

        Parameters
        ----------
        name: string
            string based on which name is generated (not equal to actual file
            name)
        path: string
            path where the file is to be located
        """
        self.name = name
        self.path = path

    def setImpedancesInTree(self, many_freqs=False, recompute=False, pprint=False):
        """
        Sets the impedances in the tree.

        Parameters
        ----------
        many_freqs: bool (optional, default is ``False``)
            If ``True``, evaluates the impedances over an array suitable to
            apply the inverse Fourrier transform to obtain temporal kernel
            If ``False``, evaluates at zero frequency
        recompute: bool (optional, default is ``False``)
            Force the impedances to be recomputed
        pprint: bool (optional, default is ``False``)
            Print info
        """
        if pprint:
            print('>>> evaluating impedances with ' + str(list(self.channel_storage.keys())))

        if many_freqs:
            freqs = ke.create_logspace_freqarray()
            suffix = 'allfreqs_'
        else:
            freqs = np.array([0.])
            suffix = ''

        e_h_string = '_eh=%.2f'%(self.root.e_eq)

        # create suffix for state variable expansion point if it is specified
        cname_string = ''
        for c_name, channel in self.channel_storage.items():
            cname_string += '_' + c_name + '_'
            try:
                sv_h = self.root.expansion_points[c_name]
                for svar in channel.ordered_statevars:
                    sv = sv_h[str(svar)]
                    cname_string += str(svar) + '=%.8f'%sv
            except (KeyError, TypeError):
                pass

        file_name = 'GF_' + suffix + self.name + e_h_string + cname_string + '.p'

        # check if impedances already exist
        try:
            # ensure that the tree is recomputed if 'recompute' is true
            if recompute:
                raise IOError
            file = open(self.path + file_name, 'rb')
            tree = pickle.load(file)
            self.__dict__.update(tree.__dict__)
            file.close()
            del tree
        except (Exception, IOError, EOFError, KeyError) as err:
            if pprint: print('>>>>>Impedances not stored, calculating...')
            self.setCompTree()
            # set the impedances
            self.setImpedance(freqs, pprint=pprint)

            if not 'dont save' in self.name:
                # store the impedance tree
                file = open(self.path + file_name, 'wb')
                pickle.dump(self, file)
                file.close()

    def calcNETSteadyState(self, root_loc=None, dx=5., dz=5.):
        if root_loc is None: root_loc = (1, .5)
        root_loc = MorphLoc(root_loc, self)
        # distribute locs on nodes
        st_nodes = self.gatherNodes(self[root_loc['node']])
        d2s_loc = self.pathLength(root_loc, (1,0.5))
        net_locs = self.distributeLocsOnNodes(d2s=np.arange(d2s_loc, 5000., dx),
                                   node_arg=st_nodes, name='net eval')
        # compute the impedance matrix for net calculation
        z_mat = self.calcImpedanceMatrix('net eval', explicit_method=False)[0]
        # assert np.allclose(z_mat, z_mat_)
        # derive the NET
        net = NET()
        self._addNodeToNET(0., z_mat[0,0], z_mat, np.arange(z_mat.shape[0]), None, net,
                           alpha=1., dz=dz)
        net.setNewLocInds()

        return net, z_mat

    def _addNodeToNET(self, z_min, z_max, z_mat, loc_inds, pnode, net, alpha=1., dz=20.):
        # compute mean impedance of node
        inds = [[]]
        while len(inds[0]) == 0:
            inds = np.where((z_mat > z_min) & (z_mat < z_max))
            z_max += dz
        z_node = np.mean(z_mat[inds])
        # subtract impedances of parent nodes
        gammas = np.array([z_node])
        self._subtractParentKernels(gammas, pnode)
        # add a node to the tree
        node = NETNode(len(net), loc_inds, z_kernel=(np.array([alpha]), gammas))
        if pnode != None:
            net.addNodeWithParent(node, pnode)
        else:
            net.root = node
        # recursion for following nodes
        d_inds = consecutive(np.where(np.diag(z_mat) > z_max)[0])
        for di in d_inds:
            if len(di) > 0:
                self._addNodeToNET(z_max, z_max+dz, z_mat[di,:][:,di], loc_inds[di], node, net,
                                       alpha=alpha, dz=dz)

    def _subtractParentKernels(self, gammas, pnode):
        if pnode != None:
            gammas -= pnode.z_kernel['c']
            self._subtractParentKernels(gammas, pnode.parent_node)


class FitTreeSOV(SOVTree):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setName('dont save', '')

    def setName(self, name, path):
        """
        Set the name and path under which the tree will be stored

        Parameters
        ----------
        name: string
            string based on which name is generated (not equal to actual file
            name)
        path: string
            path where the file is to be located
        """
        self.name = name
        self.path = path

    def setSOVInTree(self, recompute=False, pprint=False, maxspace_freq=100.):
        file_name = 'SOV_' + self.name + '.p'
        # load or compute the separation of variables tree
        try:
            # ensure that the tree is recomputed if 'recompute' is true
            if recompute:
                raise IOError
            file = open(self.path + file_name, 'rb')
            tree = pickle.load(file)
            self.__dict__.update(tree.__dict__)
            file.close()
            del tree
        except (IOError, EOFError, KeyError) as err:
            suffix = self.path + file_name if not 'dont save' in self.name else ''
            if pprint: print('>>>>> Calculating SOV expansion... ' + suffix)
            # set the computational tree
            self.setCompTree(eps=1.)
            # compute SOV factorisation
            self.calcSOVEquations(maxspace_freq=maxspace_freq, pprint=False)
            if not 'dont save' in self.name:
                # store the tree
                file = open(self.path + file_name, 'wb')
                pickle.dump(self, file)
                file.close()


class CompartmentFitter(object):
    """
    Helper class to streamline fitting reduced compartmental models

    Attributes
    ----------
    tree: `neat.PhysTree()`
        The full tree based on which reductions are made
    e_hs: np.array of float
        The holding potentials for which quasi active expansions are computed
    freqs: np.array of float or complex (default is ``np.array([0.])``)
        The frequencies at which impedance matrices are evaluated
    name: str (default 'dont save')
        name of files in which intermediate trees required for the fit are
        stored. Details about what is in the actual pickle
        files are appended as a suffix to `name`. Default is to not store
        intermediate files.
    path: str (default '')
        specify a path under which the intermediate files are saved (only if
        `name` is specified). Default is empty string, which means that
        intermediate files are stored in the working directory.
    """

    def __init__(self, phys_tree,
                 e_hs=np.array([-75., -55., -35., -15.]), freqs=np.array([0.]),
                 name='dont save', path=''):
        self.tree = phys_tree.__copy__(new_tree=PhysTree())
        self.tree.treetype = 'original'
        # get all channels in the tree
        self.channel_names = self.tree.getChannelsInTree()
        # frequencies for fit
        self.freqs = freqs
        # expansion point holding potentials for fit
        self.e_hs = e_hs
        # name to store fit models
        self.name = name
        self.path = path

        # boolean flag that is reset the first time `self.fitPassive` is called
        self.use_all_channels_for_passive = True

    def setCTree(self, loc_arg, extend_w_bifurc=True):
        """
        Store an initial `neat.CompartmentTree`, providing a tree
        structure scaffold for the fit for a given set of locations. The
        locations are also stored on ``self.tree`` under the name 'fit locs'

        Parameters
        ----------
        loc_arg: list of locations or string (see documentation of
                :func:`MorphTree._convertLocArgToLocs` for details)
            The compartment locations
        extend_w_bifurc: bool (optional, default `True`)
            To extend the compartment locations with all intermediate
            bifurcations (see documentation of
            :func:`MorphTree.extendWithBifurcationLocs`).
        """
        locs = self.tree._parseLocArg(loc_arg)
        if extend_w_bifurc:
            locs = self.tree.extendWithBifurcationLocs(locs)
        else:
            warnings.warn('Not adding bifurcations to `loc_arg`, this could '+ \
                          'lead to inaccurate fits. To add bifurcation, set' + \
                          'kwarg `extend_w_bifurc` to ``True``')
        self.tree.storeLocs(locs, name='fit locs')
        # create the reduced compartment tree
        self.ctree = self.tree.createCompartmentTree(locs)
        # add currents to compartmental model
        for c_name, channel in self.tree.channel_storage.items():
            e_revs = []
            for node in self.tree:
                if c_name in node.currents:
                    e_revs.append(node.currents[c_name][1])
            # reversal potential is the same throughout the reduced model
            self.ctree.addCurrent(copy.deepcopy(channel), np.mean(e_revs))
        # set the equilibirum potentials at fit locations
        self.setEEq()

    def createTreeGF(self, channel_names=[]):
        """
        Create a `FitTreeGF` copy of the old tree, but only with the
        channels in ``channel_names``. Leak 'L' is included in the tree by
        default.

        Parameters
        ----------
        channel_names: list of strings
            List of channel names of the channels that are to be included in the
            new tree.

        Returns
        -------
        `FitTreeGF()`

        """
        # create new tree and empty channel storage
        tree = self.tree.__copy__(new_tree=FitTreeGF())
        tree.channel_storage = {}
        tree.setName(self.name, self.path)
        # add the ion channel to the tree
        channel_names_newtree = set()
        for node, node_orig in zip(tree, self.tree):
            node.currents = {}
            g_l, e_l = node_orig.currents['L']
            # add the current to the tree
            node._addCurrent('L', g_l, e_l)
            for channel_name in channel_names:
                try:
                    g_max, e_rev = node_orig.currents[channel_name]
                    node._addCurrent(channel_name, g_max, e_rev)
                    channel_names_newtree.add(channel_name)
                except KeyError:
                    pass

        tree.channel_storage = {channel_name: self.tree.channel_storage[channel_name] \
                                for channel_name in channel_names_newtree}
        tree.setCompTree()

        return tree

    def evalChannel(self, channel_name,
                          recompute=False, pprint=False, parallel=True, max_workers=None):
        """
        Evaluate the impedance matrix for the model restricted to a single ion
        channel type.

        Parameters
        ----------
        channel_name: string
            The name of the ion channel under consideration
        recompute: bool (optional, defaults to ``False``)
            whether to force recomputing the impedances
        pprint:  bool (optional, defaults to ``False``)
            whether to print information
        parallel:  bool (optional, defaults to ``True``)
            whether the models are evaluated in parallel

        Return
        ------
        fit_mats
        """
        locs = self.tree.getLocs('fit locs')
        # find the expansion point parameters for the channel
        channel = self.tree.channel_storage[channel_name]
        sv_hs, e_hs = getExpansionPoints(self.e_hs, channel)
        n_tree = len(e_hs)

        # create the trees with only a single channel
        fit_tree = self.createTreeGF([channel_name])
        fit_tree.setName(self.name, self.path)
        fit_trees = []
        for sv_h, e_h in zip(sv_hs, e_hs):
            ftree = fit_tree.__copy__(new_tree=FitTreeGF())
            ftree.setExpansionPointsForFit({channel_name: sv_h}, e_h)
            fit_trees.append(ftree)

        # compute the impedance matrices for different activation levels
        args_list = [fit_trees,
                     [locs for _ in range(n_tree)],
                     [recompute for _ in range(n_tree)],
                     [pprint for _ in range(n_tree)]]
        # compute the impedance matrices
        if parallel:
            if max_workers is None:
                raise ValueError('need to provide number of workers if parallel is True')
            with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as pool:
                fit_mats = list(pool.map(self._calcFitMatrices, *args_list))
        else:
            fit_mats = [self._calcFitMatrices(*args) for args in zip(*args_list)]

        # fit the model for this channel
        w_norm = 1. / np.sum([w_f for _, _, w_f in fit_mats])
        for _, _, w_f in fit_mats: w_f /= w_norm

        return fit_mats

    def _calcFitMatrices(self, fit_tree, locs, recompute, pprint):
        """
        Compute the matrices needed to fit the channel
        """
        e_h = fit_tree.root.e_eq
        c_name = list(fit_tree.channel_storage.keys())[0]
        sv_h = fit_tree.root.expansion_points[c_name]
        freqs = self.freqs
        # set the impedances in the tree
        fit_tree.setImpedancesInTree(recompute=recompute, pprint=pprint)
        # compute the impedance matrix for this acitvation level
        z_mat = fit_tree.calcImpedanceMatrix(locs)

        # compute the fit matrices
        m_f, v_t = self.ctree.computeGSingleChanFromImpedance(c_name, z_mat, e_h, freqs,
                        sv=sv_h, other_channel_names=['L'],
                        all_channel_names=self.channel_names, action='return')
        # compute open probability to weigh fit matrices
        channel = self.tree.channel_storage[c_name]
        po_h = channel.computePOpen(e_h, **sv_h)
        w_f = 1. / po_h

        return m_f, v_t, w_f

    def fitChannels(self, recompute=False, pprint=False, parallel=True):
        """
        Fit the active ion channel parameters

        Parameters
        ----------
        recompute: bool (optional, defaults to ``False``)
            whether to force recomputing the impedances
        pprint:  bool (optional, defaults to ``False``)
            whether to print information
        parallel:  bool (optional, defaults to ``True``)
            whether the models are evaluated in parallel
        """
        # create the fit matrices for each channel
        n_arg = len(self.channel_names)

        if n_arg > 0:
            args_list = [self.channel_names,
                         [recompute for _ in range(n_arg)],
                         [pprint for _ in range(n_arg)],
                         [parallel for _ in range(n_arg)],
                        ]
            if parallel:
                max_workers = min(n_arg, cpu_count())
                # split cores evenly over inner workers
                inner_max_workers = cpu_count() // max_workers
                args_list += [[inner_max_workers for _ in range(n_arg)]]
                with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as pool:
                    fit_mats_ = list(pool.map(self.evalChannel, *args_list))
            else:
                fit_mats_ = [self.evalChannel(*args) for args in zip(*args_list)]
            fit_mats = [f_m for f_ms in fit_mats_ for f_m in f_ms]
            # store the fit matrices
            for m_f, v_t, w_f in fit_mats:
                if not (np.isnan(m_f).any() or np.isnan(v_t).any() or np.isnan(w_f).any()):
                    self.ctree._fitResAction('store', m_f, v_t, w_f,
                                             channel_names=self.channel_names)
            # run the fit
            self.ctree.runFit()

        # chan_eval = ChannelEvaluator()
        # chan_eval.evaluate(self, recompute=recompute, pprint=pprint, parallel=parallel)

    def fitPassive(self, use_all_channels=True, recompute=False, pprint=False):
        """
        Fit the steady state passive model, consisting only of leak and coupling
        conductances, but ensure that the coupling conductances takes the passive
        opening of all channels into account

        Parameters
        ----------
        use_all_channels: bool (optional)
            use leak at rest of all channels combined in the passive fit (passive
            leak has to be refit after capacitance fit)
        recompute: bool (optional, defaults to ``False``)
            whether to force recomputing the impedances
        pprint:  bool (optional, defaults to ``False``)
            whether to print information

        """
        self.use_all_channels_for_passive = use_all_channels

        # get equilibirum potentials
        v_eqs_tree = self.getEEq('tree')
        v_eqs_fit = self.getEEq('fit')

        locs = self.tree.getLocs('fit locs')
        # initialize appropriate greens tree
        channel_names = list(self.tree.channel_storage.keys()) if use_all_channels \
                                                               else []
        fit_tree = self.createTreeGF(channel_names)
        fit_tree.setEEq(v_eqs_tree)
        fit_tree.setName(self.name + '_atRest_', self.path)
        # set the channels to passive
        fit_tree.asPassiveMembrane()
        # set the impedances in the tree
        fit_tree.setImpedancesInTree(recompute=recompute, pprint=pprint)
        # compute the steady state impedance matrix
        z_mat = fit_tree.calcImpedanceMatrix(locs)[0].real
        # fit the coupling+leak conductances to steady state impedance matrix
        self.ctree.computeGMC(z_mat, channel_names=['L'])

        # print passive impedance matrices
        if pprint:
            z_mat_fit = self.ctree.calcImpedanceMatrix(channel_names=['L'])
            np.set_printoptions(precision=2, edgeitems=10, linewidth=500, suppress=True)
            print('\n----- Impedance matrix comparison -----')
            print('> Zmat orig =')
            print(z_mat)
            print('> Zmat fit  =')
            print(z_mat_fit)
            print('> Zmat diff =')
            print(z_mat - z_mat_fit)
            print('---------------------------------------\n')
            # restore defaults
            np.set_printoptions(precision=8, edgeitems=3, linewidth=75, suppress=False)

    def fitPassiveLeak(self, recompute=False, pprint=True):
        """
        Fit leak only. Coupling conductances have to have been fit already.

        Parameters
        ----------
        recompute: bool (optional, defaults to ``False``)
            whether to force recomputing the impedances
        pprint:  bool (optional, defaults to ``False``)
            whether to print information
        """
        locs = self.tree.getLocs('fit locs')
        # compute the steady state impedance matrix
        fit_tree = self.createTreeGF([])
        fit_tree.setName(self.name + '_onlyL_', self.path)
        # set the impedances in the tree
        fit_tree.setImpedancesInTree(recompute=recompute, pprint=pprint)
        # compute the steady state impedance matrix
        z_mat = fit_tree.calcImpedanceMatrix(locs)
        # fit the conductances to steady state impedance matrix
        self.ctree.computeGSingleChanFromImpedance('L', z_mat, -75., self.freqs,
                                                   other_channel_names=[],
                                                   action='fit')
        # print passive impedance matrices
        if pprint:
            z_mat_fit = self.ctree.calcImpedanceMatrix(channel_names=['L'])
            np.set_printoptions(precision=2, edgeitems=10, linewidth=500, suppress=True)
            print('\n----- Impedance matrix comparison -----')
            print('> Zmat orig =')
            print(z_mat)
            print('> Zmat fit  =')
            print(z_mat_fit)
            print('> Zmat diff =')
            print(z_mat - z_mat_fit)
            print('---------------------------------------\n')
            # restore defaults
            np.set_printoptions(precision=8, edgeitems=3, linewidth=75, suppress=False)

    def createTreeSOV(self, eps=1.):
        """
        Create a `SOVTree` copy of the old tree

        Parameters
        ----------
        channel_names: list of strings
            List of channel names of the channels that are to be included in the
            new tree

        Returns
        -------
        `neat.tools.fittools.compartmentfitter.FitTreeSOV`

        """
        # create new tree and empty channel storage
        tree = self.tree.__copy__(new_tree=FitTreeSOV())
        if self.use_all_channels_for_passive:
            tree.setName(self.name + '_allchans_', self.path)
        else:
            tree.setName(self.name, self.path)

        if not self.use_all_channels_for_passive:
            tree.channel_storage = {}

            for node, node_orig in zip(tree, self.tree):
                node.currents = {}
                g_l, e_l = node_orig.currents['L']
                # add the current to the tree
                node._addCurrent('L', g_l, e_l)

        # set the computational tree
        tree.setCompTree(eps=eps)

        return tree

    def _calcSOVMats(self, locs, recompute=False, pprint=False):
        """
        Use a `neat.SOVTree` to compute SOV matrices for fit
        """
        # create an SOV tree
        sov_tree = self.createTreeSOV()
        # compute the SOV expansion for this tree
        sov_tree.setSOVInTree(recompute=recompute, pprint=pprint)
        # get SOV constants
        alphas, phimat, importance = sov_tree.getImportantModes(locarg=locs,
                                            sort_type='importance', eps=1e-12,
                                            return_importance=True)
        alphas = alphas.real
        phimat = phimat.real

        return alphas, phimat, importance, sov_tree

    def fitCapacitance(self, inds=[0], check_fit=True, force_tau_m_fit=False,
                             recompute=False, pprint=False, pplot=False):
        """
        Fit the capacitances of the model to the largest SOV time scale

        Parameters
        ----------
        inds: list of int (optional, defaults to ``[0]``)
            indices of eigenmodes used in the fit. Default is [0], indicating
            the largest eigenmode
        check_fit: bool (optional, default ``True``)
            Check whether the largest eigenmode of the reduced model is within
            tolerance of the largest eigenmode of the full tree. If not,
            capacitances are set to mach membrane time scale
        force_tau_m_fit: bool (optional, default ``False``)
            force capacitance fit through membrance time scale matching
        recompute: bool (optional, defaults to ``False``)
            whether to force recomputing the impedances
        pprint:  bool (optional, defaults to ``False``)
            whether to print information
        pplot: bool (optional, defaults to ``False``)
            whether to plot the eigenmode timescales
        """
        # compute SOV matrices for fit
        locs = self.tree.getLocs('fit locs')
        alphas, phimat, importance, sov_tree = \
                self._calcSOVMats(locs, recompute=recompute, pprint=pprint)

        # fit the capacitances from SOV time-scales
        self.ctree.computeC(-alphas[inds]*1e3, phimat[inds,:],
                            weights=importance[inds])

        def calcTau():
            nm = len(locs)
            # original timescales
            taus_orig = np.sort(np.abs(1./alphas))[::-1][:nm]
            # fitted timescales
            lambdas, _, _ = self.ctree.calcEigenvalues()
            taus_fit = np.sort(np.abs(1./lambdas))[::-1]

            return taus_orig, taus_fit

        def calcTauM():
            clocs = [locs[n.loc_ind] for n in self.ctree]
            # original membrane time scales
            taus_m = []
            for l in clocs:
                g_m = sov_tree[l[0]].getGTot(channel_storage=sov_tree.channel_storage)
                taus_m.append(self.tree[l[0]].c_m / g_m *1e3)
            taus_m_orig = np.array(taus_m)
            # fitted membrance time scales
            taus_m_fit = np.array([node.ca / node.currents['L'][0]
                                   for node in self.ctree]) *1e3

            return taus_m_orig, taus_m_fit

        taus_orig, taus_fit = calcTau()
        if (check_fit and np.abs(taus_fit[0] - taus_orig[0]) > .8*taus_orig[0]) or \
           force_tau_m_fit:

            taus_m_orig, taus_m_fit = calcTauM()
            # if fit was not sane, revert to more basic membrane timescale match
            for ii, node in enumerate(self.ctree):
                node.ca = node.currents['L'][0] * taus_m_orig[ii] * 1e-3

            warnings.warn('No sane capacitance fit achieved for this configuragion,' + \
                          'reverted to more basic membrane time scale matching.')

        if pprint:
            # mode time scales
            taus_orig, taus_fit = calcTau()
            # membrane time scales
            taus_m_orig, taus_m_fit = calcTauM()

            np.set_printoptions(precision=2, edgeitems=10, linewidth=500, suppress=False)
            print('\n----- capacitances -----')
            print(('Ca (uF) =\n' + str([nn.ca for nn in self.ctree])))
            print('\n----- Eigenmode time scales -----')
            print(('> Taus original (ms) =\n' + str(taus_orig)))
            print(('> Taus fitted (ms) =\n' + str(taus_fit)))
            print('\n----- Membrane time scales -----')
            print(('> Tau membrane original (ms) =\n' + str(taus_m_orig)))
            print(('> Tau membrane fitted (ms) =\n' + str(taus_m_fit)))
            print('---------------------------------\n')
            # restore default print options
            np.set_printoptions(precision=8, edgeitems=3, linewidth=75, suppress=False)

        else:
            lambdas = None

        if pplot:
            self.plotKernels(alphas, phimat)

    def plotSOV(self, alphas=None, phimat=None, importance=None, n_mode=8, alphas2=None):
        fit_locs = self.tree.getLocs('fit locs')

        if alphas is None or phimat is None or importance is None:
            alphas, phimat, importance, _ = self._calcSOVMats(fit_locs,
                                            recompute=False, pprint=False)
        if alphas2 is None:
            alphas2, _, _ = self.ctree.calcEigenvalues()

        fit_locs = self.tree.getLocs('fit locs')
        colours = list(pl.rcParams['axes.prop_cycle'].by_key()['color'])
        loc_colours = np.array([colours[ii%len(colours)] for ii in range(len(fit_locs))])
        markers = Line2D.filled_markers

        pl.figure('SOV', figsize=(10,10))
        gs = GridSpec(2,2)
        ax1, ax2, ax3 = pl.subplot(gs[0,0]), pl.subplot(gs[0,1]), pl.subplot(gs[1,:])
        # x axis modes
        x_arr = np.arange(n_mode)
        x_loc = np.arange(len(fit_locs))
        # time scales
        ax1.semilogy(x_arr, np.abs(1./alphas[:n_mode]), 'rD--')
        if alphas2 is not None:
            ax1.semilogy(x_arr[:len(alphas2)], np.sort(np.abs(1./alphas2))[::-1], 'bo--')
        ax1.set_xlabel(r'$k$')
        ax2.set_ylabel(r'$\tau_k$ (ms)')
        # importance
        ax2.semilogy(x_arr, importance[:n_mode], 'rD--')
        ax2.set_xlabel(r'$k$')
        ax2.set_ylabel(r'$I_k$')
        # spatial modes
        for kk in range(n_mode):
            ax3.plot(x_loc, phimat[kk,:], ls='--', c='DarkGrey')
            ax3.scatter(x_loc, phimat[kk,:], c=loc_colours, marker=markers[kk%len(markers)], label=r''+str(kk))
        ax3.set_xlabel(r'$x_i$')
        ax3.set_ylabel(r'$\phi_k(x_i)$')
        ax3.legend(loc=0)

    def _constructKernels(self, a, c):
        nn = len(self.tree.getLocs('fit locs'))
        return [[Kernel((a, c[:,ii,jj])) for ii in range(nn)] for jj in range(nn)]

    def _getKernels(self, alphas=None, phimat=None,
                          recompute=False, pprint=False):
        """
        Returns the impedance kernels as a double nested list of "neat.Kernel".
        The element at the position i,j represents the transfer impedance kernel
        between compartments i and j.

        If one of the arguments is not given, the SOV matrices are computed

        Parameters
        ----------
        alphas: np.array
            The exponential coefficients, as follows from the SOV expansion
        phimat: np.ndarray (dim=2)
            The matrix to compute the exponential prefactors, as follows from
            the SOV expansion
        recompute: bool
            Force recomputing the SOV expansion if ``True`` (only if `alphas` or
            `phimat` are ``None``)
        pprint: bool
            Is verbose if ``True``

        Returns
        -------
        k_orig: list of list of `neat.Kernel`
            The kernels of the full model
        k_comp: list of list of `neat.Kernel`
            The kernels of the reduced model
        """
        fit_locs = self.tree.getLocs('fit locs')
        if alphas is None or phimat is None:
            alphas, phimat, _, _ = self._calcSOVMats(fit_locs, recompute=recompute, pprint=pprint)

        # compute eigenvalues
        alphas_comp, phimat_comp, phimat_inv_comp = \
                                self.ctree.calcEigenvalues(indexing='locs')

        # get the kernels
        k_orig = self._constructKernels(alphas, np.einsum('ik,kj->kij', phimat.T, phimat))
        k_comp = self._constructKernels(-alphas_comp, np.einsum('ik,kj->kij', phimat_comp, phimat_inv_comp))

        return k_orig, k_comp

    def getKernels(self, recompute=False, pprint=False):
        """
        Returns the impedance kernels as a double nested list of "neat.Kernel".
        The element at the position i,j represents the transfer impedance kernel
        between compartments i and j.

        Parameters
        ----------
        recompute: bool
            Force recomputing the SOV expansion if ``True``
        pprint: bool
            Is verbose if ``True``

        Returns
        -------
        k_orig: list of list of `neat.Kernel`
            The kernels of the full model
        k_comp: list of list of `neat.Kernel`
            The kernels of the reduced model
        """
        return self._getKernels(recompute=recompute, pprint=pprint)

    def plotKernels(self, alphas=None, phimat=None, t_arr=None,
                          recompute=False, pprint=False):
        """
        Plots the impedance kernels.
        The kernel at the position i,j represents the transfer impedance kernel
        between compartments i and j.

        Parameters
        ----------
        alphas: np.array
            The exponential coefficients, as follows from the SOV expansion
        phimat: np.ndarray (dim=2)
            The matrix to compute the exponential prefactors, as follows from
            the SOV expansion
        t_arr: np.array
            The time-points at which the to be plotted kernels are evaluated.
            Default is ``np.linspace(0.,200.,int(1e3))``
        recompute: bool
            Force recomputing the SOV expansion if ``True`` (only if `alphas` or
            `phimat` are ``None``)
        pprint: bool
            Is verbose if ``True``

        Returns
        -------
        k_orig: list of list of `neat.Kernel`
            The kernels of the full model
        k_comp: list of list of `neat.Kernel`
            The kernels of the reduced model
        """
        fit_locs = self.tree.getLocs('fit locs')
        nn = len(fit_locs)

        k_orig, k_comp = self._getKernels(alphas=alphas, phimat=phimat)

        if t_arr is None:
            t_arr = np.linspace(0.,200.,int(1e3))

        pl.figure('Kernels', figsize=(2.*nn, 1.5*nn))
        gs = GridSpec(nn, nn)
        gs.update(top=0.98, bottom=0.04, left=0.04, right=0.98)
        colours = list(pl.rcParams['axes.prop_cycle'].by_key()['color'])
        loc_colours = np.array([colours[ii%len(colours)] for ii in range(len(fit_locs))])

        for ii in range(nn):
            for jj in range(ii, nn):
                ko, kc = k_orig[ii][jj], k_comp[ii][jj]
                ax = pl.subplot(gs[ii,jj])
                ax.plot(t_arr, ko(t_arr), c='DarkGrey')
                ax.plot(t_arr, kc(t_arr), ls='--', c=loc_colours[jj])
                # limits
                ax.set_ylim((-0.5, 20.))
                # kernel label
                pstring = '%d $\leftrightarrow$ %d'%(ii,jj)
                ax.set_title(pstring, pad=-10)

    def checkPassive(self, loc_arg, alpha_inds=[0], n_modes=5,
                           use_all_channels_for_passive=True, force_tau_m_fit=False,
                           recompute=False, pprint=False):
        """
        Checks the impedance kernels of the passive model.

        Parameters
        ----------
        loc_arg: list of locations or string (see documentation of
                :func:`MorphTree._convertLocArgToLocs` for details)
            The compartment locations
        alpha_inds: list of ints
            Indices of all mode time-scales to be included in the fit
        n_modes: int
            The number of eigen modes that are shown
        use_all_channels_for_passive: bool
            Uses all channels in the tree to compute coupling conductances
        force_tau_m_fit: bool
            Force using the local membrane time-scale for capacitance fit
        recompute: bool
            whether to force recomputing the impedances
        pprint: bool
            is verbose if ``True``

        Returns
        -------
        ``None``
        """
        self.setCTree(loc_arg)
        # fit the passive steady state model
        self.fitPassive(recompute=recompute, use_all_channels=use_all_channels_for_passive,
                        pprint=pprint)
        # fit the capacitances
        self.fitCapacitance(inds=alpha_inds, recompute=recompute,
                            force_tau_m_fit=force_tau_m_fit,
                            pprint=pprint, pplot=True)

        fit_locs = self.tree.getLocs('fit locs')
        colours = list(pl.rcParams['axes.prop_cycle'].by_key()['color'])
        loc_colours = np.array([colours[ii%len(colours)] for ii in range(len(fit_locs))])

        pl.figure('tree')
        ax = pl.gca()
        locargs = [dict(marker='o', mec='k', mfc=lc, markersize=6.) for lc in loc_colours]
        self.tree.plot2DMorphology(ax, marklocs=fit_locs, locargs=locargs, use_radius=False)

        pl.tight_layout()
        pl.show()

    def getNET(self, c_loc, locs, channel_names=[], recompute=False, pprint=False):
        greens_tree = self.createTreeGF(channel_names=channel_names)
        greens_tree.setImpedancesInTree(recompute=recompute, pprint=False)
        # create the NET
        net, z_mat = greens_tree.calcNETSteadyState(c_loc)
        net.improveInputImpedance(z_mat)

        # prune the NET to only retain ``locs``
        loc_inds = greens_tree.getNearestLocinds([c_loc]+locs, 'net eval')
        net_reduced = net.getReducedTree(loc_inds, indexing='locs')

        return net_reduced

    def calcEEq(self, locs, t_max=500., dt=0.1, factor_lambda=10.):
        # create a biophysical simulation model
        sim_tree_biophys = self.tree.__copy__(new_tree=neurm.NeuronSimTree())
        # compute equilibrium potentials
        sim_tree_biophys.initModel(dt=dt, factor_lambda=factor_lambda)
        sim_tree_biophys.storeLocs(locs, 'rec locs', warn=False)
        res_biophys = sim_tree_biophys.run(t_max)
        sim_tree_biophys.deleteModel()
        return np.array([v_m[-1] for v_m in res_biophys['v_m']])

    def setEEq(self, t_max=500., dt=0.1, factor_lambda=10.):
        """
        Set equilibrium potentials, measured from neuron simulation. Sets the
        `v_eqs_tree` and `v_eqs_fit` attributes, respectively containing the
        equilibrium potentials at (the middle of) each node in the original
        tree and at each of the fit locations

        Parameters
        ----------
        t_max: float
            duration of the neuron simulation
        dt: float
            time-step of the neuron simulation
        factor_lambda: int of float
            if int, signifies the number of segments per section. If float,
            multiplies the number of segments given by the lambda rule with this
            number
        """
        tree_locs = [MorphLoc((n.index, .5), self.tree) for n in self.tree]
        fit_locs = self.tree.getLocs('fit locs')
        # compute equilibrium potentials
        v_eqs = self.calcEEq(tree_locs + fit_locs,
                             t_max=t_max, dt=dt, factor_lambda=factor_lambda)
        # store the equilibrium potentials
        self.v_eqs_tree = {n.index: v for n, v in zip(self.tree, v_eqs)}
        self.v_eqs_fit = v_eqs[len(tree_locs):]

    def getEEq(self, e_eqs_type, **kwargs):
        """
        Get equilibrium potentials. Specify
        `v_eqs_tree` and `v_eqs_fit` attributes, respectively containing the
        equilibrium potentials at (the middle of) each node in the original
        tree and at each of the fit locations

        Parameters
        ----------
        e_eqs_type: 'tree' or 'fit'
            For 'tree', returns the `v_eqs_tree` attribute, containing the
            equilibrium potentials at (the middle of) each node in the original
            tree. For 'fit', returns the `v_eqs_fit` attribute, containing the
            equilibrium potentials at each of the fit locations.
        kwargs: When `v_eqs_tree` or `v_eqs_fit`, have not been set, calls
            ::func::`self.setEEq()` with these `kwargs`

        """
        if not hasattr(self, 'v_eqs_tree') or not hasattr(self, 'v_eqs_fit'):
            self.setEEq(**kwargs)
        if e_eqs_type == 'fit':
            return self.v_eqs_fit
        elif e_eqs_type == 'tree':
            return self.v_eqs_tree
        else:
            raise IOError('``e_eqs_type`` should be \'fit\' or \'tree\'')

    def fitEEq(self, **kwargs):
        """
        Fits the leak potentials of the reduced model to yield the same
        equilibrium potentials as the full model

        Parameters
        ----------
        kwargs: When `v_eqs_tree` or `v_eqs_fit`, have not been set, calls
            ::func::`self.setEEq()` with these `kwargs`
        """
        # compute equilibirum potentials
        v_eqs = self.getEEq('fit', **kwargs)
        # fit the equilibirum potentials of the reduced model
        self.ctree.setEEq(v_eqs)
        self.ctree.fitEL()

    def fitModel(self, loc_arg, alpha_inds=[0], use_all_channels_for_passive=True,
                       recompute=False, pprint=False, parallel=False):
        """
        Runs the full fit for a set of locations (the location are automatically
        extended with the bifurcation locs)

        Parameters
        ----------
        loc_arg: list of locations or string (see documentation of
                :func:`MorphTree._convertLocArgToLocs` for details)
            The compartment locations
        alpha_inds: list of ints
            Indices of all mode time-scales to be included in the fit
        use_all_channels_for_passive: bool (optional, default ``True``)
            Uses all channels in the tree to compute coupling conductances
        recompute: bool
            whether to force recomputing the impedances
        pprint:  bool
            whether to print information
        parallel:  bool
            whether the models are evaluated in parallel

        Returns
        -------
        `neat.CompartmentTree`
            The reduced tree containing the fitted parameters
        """
        self.setCTree(loc_arg)
        # fit the passive steady state model
        self.fitPassive(recompute=recompute, pprint=pprint,
                        use_all_channels=use_all_channels_for_passive)
        # fit the capacitances
        self.fitCapacitance(inds=alpha_inds,
                            recompute=recompute, pprint=pprint, pplot=False)
        # refit with only leak
        if use_all_channels_for_passive:
            self.fitPassiveLeak(recompute=recompute, pprint=pprint)

        # fit the ion channel
        self.fitChannels(recompute=recompute, pprint=pprint, parallel=parallel)
        # fit the resting potentials
        self.fitEEq()

        return self.ctree

    def recalcImpedanceMatrix(self, locarg, g_syns,
                              channel_names=None, recompute=False):
        # process input
        locs = self.tree._parseLocArg(locarg)
        n_syn = len(locs)
        assert n_syn == len(g_syns)
        if n_syn == 0:
            return np.array([[]])
        if channel_names is None:
            channel_names = list(self.tree.channel_storage.keys())

        # compute equilibirum potentials
        all_locs = [(n.index, .5) for n in self.tree]
        e_eqs = self.calcEEq(all_locs + locs)
        # create a greenstree with equilibrium potentials at rest
        greens_tree = self.createTreeGF(channel_names=channel_names)
        greens_tree.setName(self.name + '_atRest_', self.path)
        for ii, node in enumerate(greens_tree):
            node.setEEq(e_eqs[ii])
        greens_tree.setImpedancesInTree(recompute=recompute, pprint=False)
        # compute the impedance matrix of the synapse locations
        z_mat = greens_tree.calcImpedanceMatrix(locs, explicit_method=False)[0].real

        # get the reversal potentials of the synapse locations
        n_all = len(self.tree)
        e_eqs = e_eqs[n_all:]

        # compute the ZG matrix
        gd_mat = np.diag(g_syns)
        zg_mat = np.dot(z_mat, gd_mat)
        z_mat_ = np.linalg.solve(np.eye(n_syn) + zg_mat, z_mat)

        return z_mat_

    def fitSynRescale(self, c_locarg, s_locarg, comp_inds, g_syns, e_revs,
                            fit_impedance=False, channel_names=None, recompute=False):
        """
        Computes the rescaled conductances when synapses are moved to compartment
        locations, assuming a given average conductance for each synapse.

        Parameters
        ----------
        c_locarg: list of locations or string (see documentation of
                  :func:`MorphTree._convertLocArgToLocs` for details)
            The compartment locations
        s_locarg: list of locations or string (see documentation of
                  :func:`MorphTree._convertLocArgToLocs` for details)
            The synapse locations
        comp_inds: list or numpy.array of ints
            for each location in [s_locarg], gives the index of the compartment
            location in [c_locarg] to which the synapse is assigned
        g_syns: list or numpy.array of floats
            The average conductances for each synapse
        e_revs: list or numpy.array of floats
            The reversal potential of each synapse
        fit_impdedance: bool (optional, default `False`)
            Whether to also use the reproduction of the rescaled impedance matrix
            as target.
        channel_names: list of str or `None` (default)
            List of ion channels to be included in impedance matrix calculation.
            `None` includes all ion channels
        recompute: bool (defaults is `False`)
            Whether or not to recompute the impedance tree for this channel
            configuration

        Returns
        -------
        g_resc: numpy.array of floats
            The rescale values for the synaptic weights
        """
        # process input
        c_locs = self.tree._parseLocArg(c_locarg)
        s_locs = self.tree._parseLocArg(s_locarg)
        n_comp, n_syn = len(c_locs), len(s_locs)
        assert n_syn == len(g_syns) and n_syn == len(e_revs)
        assert len(c_locs) > 0
        if n_syn == 0:
            return np.array([])
        if channel_names is None:
            channel_names = list(self.tree.channel_storage.keys())
        cs_locs = c_locs + s_locs
        cg_syns = np.concatenate((np.zeros(n_comp), np.array(g_syns)))
        comp_inds, g_syns, e_revs = np.array(comp_inds), np.array(g_syns), np.array(e_revs)

        # compute equilibirum potentials
        all_locs = [(n.index, .5) for n in self.tree]
        e_eqs = self.calcEEq(all_locs + cs_locs)
        # create a greenstree with equilibrium potentials at rest
        greens_tree = self.createTreeGF(channel_names=channel_names)
        greens_tree.setName(self.name + '_atRest_', self.path)
        for ii, node in enumerate(greens_tree):
            node.setEEq(e_eqs[ii])
        greens_tree.setImpedancesInTree(recompute=recompute, pprint=False)
        # compute the impedance matrix of the synapse locations
        z_mat = greens_tree.calcImpedanceMatrix(cs_locs, explicit_method=False)[0].real
        zc_mat = z_mat[:n_comp, :n_comp]

        # get the reversal potentials of the synapse locations
        n_all = len(self.tree)
        e_cs = e_eqs[n_all:n_all+n_comp]
        e_ss = e_eqs[-n_syn:]

        # compute the ZG matrix
        gd_mat = np.diag(cg_syns)
        zg_mat_ = np.dot(z_mat, gd_mat)
        zg_mat = np.linalg.solve(np.eye(n_comp+n_syn) + zg_mat_, zg_mat_)
        zg_mat = zg_mat[:n_comp,n_comp:]

        # create the compartment assignment matrix & syn index vector
        c_mat = np.array([comp_inds == cc for cc in range(n_comp)]).astype(int)
        s_inds = np.array([np.where(cc > 0)[0][0] for cc in c_mat.T])

        # compute the driving potential vectors
        es_vec = e_revs - e_ss
        ec_vec = e_revs - e_cs[s_inds]

        zc_mat = np.dot(zc_mat, c_mat)
        czg_mat = np.dot(c_mat.T, zg_mat)

        # create matrices for inverse fit
        a1_mat = np.einsum('ck,kn->cnk', zc_mat, np.diag(ec_vec))
        a2_mat = np.einsum('ck,kn->cnk', zc_mat, czg_mat*es_vec[None,:])
        b_mat = zg_mat * es_vec[None,:]

        # unravel first two indices
        a_mat = np.reshape(a1_mat-a2_mat, (n_syn*n_comp,-1))
        b_vec = np.reshape(b_mat, (n_syn*n_comp,))

        if fit_impedance:
            # fit based on impedance matrix
            zr_mat = np.linalg.solve(np.eye(n_comp+n_syn) + zg_mat_, z_mat)

            zr_mat = zr_mat[:n_comp,:n_comp]
            zc_mat = z_mat[:n_comp,:n_comp]

            # b matrix for fit
            b_mat = zc_mat - zr_mat
            # a tensor for fit
            zcc = np.dot(zc_mat, c_mat)
            czr = np.dot(c_mat.T, zr_mat)
            aa_mat = np.einsum('ik,kn->ink', zcc, czr)

            # unravel first two indices
            a_mat_ = np.reshape(aa_mat, (n_comp*n_comp,-1))
            b_vec_ = np.reshape(b_mat, (n_comp*n_comp,))

            # perfor mfit
            a_mat = np.concatenate((a_mat, a_mat_), axis=0)
            b_vec = np.concatenate((b_vec, b_vec_), axis=0)

        # compute rescaled synaptic conductances
        g_resc = np.linalg.lstsq(a_mat, b_vec, rcond=None)[0]

        b_arr = g_syns > 1e-9
        g_resc[np.logical_not(b_arr)] = 1.
        g_resc[b_arr] = g_resc[b_arr] / g_syns[b_arr]

        return g_resc

    def assignLocsToComps(self, c_locarg, s_locarg, fz=.8,
                                channel_names=None, recompute=False):
        """
        assumes the root node is in `c_locarg`
        """
        if channel_names is None:
            channel_names = list(self.tree.channel_storage.keys())

        # compute equilibirum potentials
        e_eqs = self.getEEq('tree')
        # create a greenstree with equilibrium potentials at rest
        greens_tree = self.createTreeGF(channel_names=channel_names)
        greens_tree.setName(self.name + '_atRest_', self.path)
        for ii, node in enumerate(greens_tree):
            node.setEEq(e_eqs[ii])
        greens_tree.setImpedancesInTree(recompute=recompute, pprint=False)

        # process input
        c_locs = self.tree._parseLocArg(c_locarg)
        s_locs = self.tree._parseLocArg(s_locarg)
        # find nodes corresponding to locs
        c_nodes = [self.tree[loc['node']] for loc in c_locs]
        s_nodes = [self.tree[loc['node']] for loc in s_locs]
        # compute input impedances
        c_zins = [greens_tree.calcZF(c_loc, c_loc)[0] for c_loc in c_locs]
        s_zins = [greens_tree.calcZF(s_loc, s_loc)[0] for s_loc in s_locs]
        # paths to root
        c_ptrs = [self.tree.pathToRoot(node) for node in c_nodes]
        s_ptrs = [self.tree.pathToRoot(node) for node in s_nodes]

        c_inds = []
        for s_node, s_path, s_loc, s_zin in zip(s_nodes, s_ptrs, s_locs, s_zins):
            z_diffs = []
            # check if there are compartment nodes before bifurcation nodes in up direction
            nn_inds = greens_tree.getNearestNeighbourLocinds(s_loc, c_locs)
            # print c_before_b
            c_ns = [c_nodes[ii] for ii in nn_inds]
            c_ps = [c_ptrs[ii] for ii in nn_inds]
            c_ls = [c_locs[ii] for ii in nn_inds]
            c_zs = [c_zins[ii] for ii in nn_inds]
            for c_node, c_path, c_loc, c_zin in zip(c_ns, c_ps, c_ls, c_zs):
                # find the common node as far from the root as possible
                s_p, c_p = s_path[::-1], c_path[::-1]
                kk = 0
                while kk < min(len(s_p), len(c_p)) and s_p[kk] == c_p[kk]:
                    p_node = s_p[kk]
                    kk += 1
                # distinguish cases for computing impedance different
                if p_node == s_node and p_node != c_node:
                    z_diffs.append(fz*np.abs(c_zin - s_zin))
                elif p_node == c_node and p_node != s_node:
                    z_diffs.append((1.-fz)*np.abs(s_zin - c_zin))
                elif p_node == c_node and p_node == s_node:
                    fz_ = fz if c_loc['x'] > s_loc['x'] else (1.-fz)
                    z_diffs.append(fz_*np.abs(s_zin-c_zin))
                else:
                    b_loc = (p_node.index, 1.)
                    b_z = greens_tree.calcZF(b_loc, b_loc)[0]
                    z_diffs.append((1.-fz)*(c_zin - b_z) + fz * (s_zin - b_z))
            # compartment node with minimal impedance difference
            ind_aux = np.argmin(z_diffs)
            c_inds.append(nn_inds[ind_aux])

        return c_inds

