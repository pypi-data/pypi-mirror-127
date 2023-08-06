"""Provides certain utilities for the streamlit demo."""

from abc import ABC, abstractmethod
from itertools import product, repeat
from typing import List, Iterable, Tuple, Optional

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from tnmf.TransformInvariantNMF import TransformInvariantNMF, MiniBatchAlgorithm
from tnmf.utils.signals import generate_pulse_train, generate_block_image

HELP_CHANNEL = \
    '''The **number of channels** each input signal comprises. In contrast to the remaining signal dimensions, which are
    treated shift-invariant (meaning that atom placement is flexible), channels represent the inflexible part of the
    factorization in the sense that each atom always covers all channels.'''


def explanation(text: str, verbose: bool):
    if verbose:
        st.sidebar.caption(text)


def st_define_nmf_params(default_params: dict, have_ground_truth: bool = True, verbose: bool = True) -> dict:
    """
    Defines all necessary NMF parameters via streamlit widgets.

    Parameters
    ----------
    default_params : dict
        Contains the default parameters that are used if the created streamlit checkbox is True.
    have_ground_truth : bool
        If True, the parameters in default_params are considered being ground truth values and
        the respective explanatory texts are modified accordingly.
    verbose : bool
        If True, show detailed information.

    Returns
    -------
    nmf_params : dict
        A dictionary containing the selected NMF parameters.
    """
    st.sidebar.markdown('# TNMF settings')

    help_n_atoms = 'The **number of atoms**.'
    if have_ground_truth:
        # decide if ground truth atom number shall be used
        help_n_atoms += ' To use the ground truth dictionary size, tick the checkbox above.'
        help_use_n_atoms = \
            '''If selected, the **number of atoms** used by the model is set to the actual number of atoms used
            for signal generation.'''
        use_n_atoms = st.sidebar.checkbox('Use ground truth number of atoms', True, help=help_use_n_atoms)
        explanation(help_use_n_atoms, verbose)
    else:
        use_n_atoms = False

    n_atoms_default = default_params['n_atoms']
    n_atoms = st.sidebar.number_input('# Atoms', value=n_atoms_default, min_value=1,
                                      help=help_n_atoms) if not use_n_atoms else n_atoms_default
    explanation(help_n_atoms, verbose and not use_n_atoms)

    help_atom_shape = 'The **size of each atom** dimension.'
    if have_ground_truth:
        # decide if ground truth atom shape shall be used
        help_atom_shape += ' To use the ground truth atom size, tick the checkbox above.'
        help_use_atom_shape = \
            '''If selected, the **size of the atoms** used by the model is set the actual size of the atoms used
            for signal generation.'''
        use_atom_shape = st.sidebar.checkbox('Use ground truth atom size', True, help=help_use_atom_shape)
        explanation(help_use_atom_shape, verbose)
    else:
        use_atom_shape = False

    default_atom_shape = default_params['atom_shape']
    atom_shape = tuple([st.sidebar.number_input('Atom size',
                        value=default_atom_shape[0], min_value=1,
                        help=help_atom_shape)] * len(default_params['atom_shape'])
                       ) if not use_atom_shape else default_atom_shape
    explanation(help_atom_shape, verbose and not use_atom_shape)

    help_sparsity_H = 'The strength of the **L1 activation sparsity regularization** imposed on the optimization problem.'
    sparsity_H = st.sidebar.number_input('Activation sparsity', min_value=0.0, value=0.0, step=0.01,
                                         help=help_sparsity_H)
    explanation(help_sparsity_H, verbose)

    help_inhibition_strength = \
        '''The strength of the **same-atom lateral activation sparsity regularization** imposed on the optimization problem.
        The parameter controls how strong the activation of an atom at a particular shift location suppresses the activation
        of *the same atom* at neighboring locations.'''
    inhibition_strength = st.sidebar.number_input('Lateral activation inhibition (same atom)',
                                                  min_value=0.0, value=0.1, step=0.01,
                                                  help=help_inhibition_strength)
    explanation(help_inhibition_strength, verbose)

    help_cross_atom_inhibition_strength = \
        '''The strength of the **cross-atom lateral activation sparsity regularization** imposed on the optimization problem.
        The parameter controls how strong the activation of an atom at a particular shift location suppresses the activation
        of *all other atoms* at the same and neighboring locations.'''
    cross_atom_inhibition_strength = st.sidebar.number_input('Lateral activation inhibition (cross-atom)',
                                                             min_value=0.0, value=0.1, step=0.01,
                                                             help=help_cross_atom_inhibition_strength)
    explanation(help_cross_atom_inhibition_strength, verbose)

    help_minibatch = \
        '''Process the samples in **minibatches** instead of the full data set at once.'''
    minibatch_updates = st.sidebar.checkbox('Minibatch updates', value=True, help=help_minibatch)
    explanation(help_minibatch, verbose)
    if not minibatch_updates:
        help_n_iterations = '''The **number of multiplicative updates** to the atom dictionary and activation tensors.'''
        n_iterations = st.sidebar.number_input('# Iterations', value=100, min_value=1, help=help_n_iterations)
        explanation(help_n_iterations, verbose)
    else:
        help_algorithm = '''The **minibatch update algorithm** to be used.'''
        algorithm = st.sidebar.radio('Minibatch algorithm', [
            '4 - Cyclic MiniBatch for MU rules',
            '5 - Asymmetric SG MiniBatch MU rules (ASG-MU)',
            '6 - Greedy SG MiniBatch MU rules (GSG-MU)',
            '7 - Asymmetric SAG MiniBatch MU rules (ASAG-MU)',
            '8 - Greedy SAG MiniBatch MU rules (GSAG-MU)'],
                                     1, help=help_algorithm)
        algorithm = MiniBatchAlgorithm(int(algorithm[0]))
        explanation(help_algorithm, verbose)

        help_epoch = '''The number of **passes through the whole data set**.'''
        n_epochs = st.sidebar.number_input('# Epochs', value=100, min_value=1, help=help_epoch)
        explanation(help_epoch, verbose)

        help_batch_size = '''The number of **samples per batch**.'''
        batch_size = st.sidebar.number_input('# Batch size', value=3, min_value=1, help=help_batch_size)
        explanation(help_batch_size, verbose)

        sag_lambda = None
        if algorithm in (MiniBatchAlgorithm.ASAG_MU, MiniBatchAlgorithm.GSAG_MU):
            help_sag_lambda = \
                '''The **exponential forgetting factor** for for the stochastic **average** gradient updates. A value of 1.0
                means that only the latest minibatch is used for the update. The smaller the value, the more weight is put on
                older minibatches.'''
            sag_lambda = st.sidebar.number_input('Lambda', min_value=0.0, max_value=1., value=0.2, step=0.01,
                                                 help=help_sag_lambda)
            explanation(help_sag_lambda, verbose)

    help_backend = \
        '''The **optimization backend** for computing the multiplicative gradients.
            **Note:** All backends yield the same results. Within the scope of this demo, switching between backends is thus
            for speed comparisons only.'''
    backend = st.sidebar.selectbox('Backend', ['numpy', 'numpy_fft', 'numpy_caching_fft', 'pytorch', 'pytorch_fft'], 4,
                                   help=help_backend)
    explanation(help_backend, verbose)

    help_reconstruction_mode = \
        '''Defines the **convolution mode** for the signal reconstruction.\

        **valid:** The activation tensor
        is smaller than the input by the atom size along the shift dimensions, so that the convolution of atoms and
        activations matches the size of the input.\

        **full:** The activation tensor is larger than the input by the atom size along the shift dimensions. Compared to the
        'valid' reconstruction mode, this also creates shifted versions of each atom that only partially overlap with the input
        array. The convolution result is trimmed to the appropriate size.\

        **circular:** The activation tensor is of the same
        size as the input. Other than in 'full' mode, parts of the convolution result that are outside the range of the
        input array are inserted circularly on the respective other side of the array.'''
    reconstruction_mode = st.sidebar.selectbox('Reconstruction', ['valid', 'full', 'circular'], 2,
                                               help=help_reconstruction_mode)
    explanation(help_reconstruction_mode, verbose)

    nmf_params = dict(
        n_atoms=n_atoms,
        atom_shape=atom_shape,
        backend=backend,
        reconstruction_mode=reconstruction_mode,
    )

    if not minibatch_updates:
        fit_params = dict(
            n_iterations=n_iterations,
            sparsity_H=sparsity_H,
            inhibition_strength=inhibition_strength,
            cross_atom_inhibition_strength=cross_atom_inhibition_strength,
        )
    else:
        fit_params = dict(
            algorithm=algorithm,
            n_epochs=n_epochs,
            batch_size=batch_size,
            sag_lambda=sag_lambda,
            sparsity_H=sparsity_H,
            inhibition_strength=inhibition_strength,
            cross_atom_inhibition_strength=cross_atom_inhibition_strength,
        )

    return nmf_params, fit_params


class SignalTool(ABC):
    """An abstract base class that serves as a factory for creating specialized objects that facilitate the handling of
    different signal types."""

    def __new__(cls, n_dims: int):
        """
        Parameters
        ----------
        n_dims : int
            The dimensionality of the signals to be managed.
            * n_dims=1 for time series.
            * n_dims=2 for image data.
        """
        if n_dims == 1:
            return super(SignalTool, cls).__new__(SignalTool1D)
        if n_dims == 2:
            return super(SignalTool, cls).__new__(SignalTool2D)
        raise ValueError("'n_dims' must be in {1, 2}")

    @classmethod
    def st_generate_input(cls, verbose: bool = True) -> Tuple[np.ndarray, dict]:
        """
        Defines all signal parameters via streamlit widgets and returns a generated input matrix V for the NMF together
        with a dictionary containing details of the used NMF atoms.

        Parameters
        ----------
        verbose : bool
            If True, show detailed information.

        Returns
        -------
        V : np.ndarray
            The generated input for the NMF.
        nmf_params : dict
            Ground truth NMF atom parameters that were used for the signal generation.
        """
        st.sidebar.markdown('# Signal settings')

        # define the number input signals
        help_n_signals = \
            '''The **number of generated signals** passed as input to the algorithm.
            All signals have the same shape and number of channels.'''
        n_signals = st.sidebar.number_input('# Signals', min_value=1, value=10, help=help_n_signals)
        explanation(help_n_signals, verbose)
        signal_params = cls.st_define_signal_params(verbose=verbose)

        # create the input
        V = []
        for _ in range(n_signals):
            signal, W = cls.generate_signal(signal_params)
            V.append(signal)
        V = np.stack(V)

        # extract the ground truth NMF parameters
        nmf_params = {'n_atoms': W.shape[0], 'atom_shape': W.shape[2:]}

        return V, nmf_params

    @classmethod
    def st_compare_signals(cls, V: np.ndarray, R: np.ndarray, verbose: bool = True):
        """
        Compares a given input matrix with its NMF reconstruction in streamlit.

        Parameters
        ----------
        V : np.ndarray
            The input that was factorized via NMF.
        R : np.ndarray
            The NMF reconstruction of the input.
        verbose : bool
            If True, show detailed information.
        """
        st.markdown('# Global signal reconstruction')

        # show explanatory text
        if verbose:
            st.caption('''The visualization below gives a **first impression of the reconstruction accuracy** of the
            learned factorization.\

            **Left**: The entire input provided to the algorithm visualized as a matrix. Each row represents a particular input
                signal, whose channels and remaining dimensions have been stacked into a single vector.\

            **Middle**: The reconstruction of the signal obtained through the learned factorization, reshaped in the same way.\

            **Right**: The difference between the two matrices.
            ''')

        # show the input, its reconstruction, and the reconstruction error as images next to each other
        cols = st.columns(3)
        for col, X, title in zip(cols, [V, R, V-R], ['Input', 'Reconstruction', 'Error']):
            with col:
                fig = plt.figure()
                plt.imshow(X.reshape(X.shape[0], -1), aspect='auto', interpolation='none')
                plt.title(title)
                st.pyplot(fig)

    @classmethod
    def st_compare_individual_signals(cls, V: np.ndarray, R: np.ndarray, verbose: bool = True):
        """
        Selects a particular signal and its reconstruction from the given input via a streamlit widget and compares them.

        Parameters
        ----------
        V : np.ndarray
            The input that was factorized via NMF.
        R : np.ndarray
            The NMF reconstruction of the input.
        verbose : bool
            If True, show detailed information.
        """
        st.markdown('# Individual signal reconstruction')

        # show explanatory text
        if verbose:
            st.caption('''The visualization below shows a **comparison between an individual input signal and its
            reconstruction** obtained through the learned factorization model. If more than one input signal has been
            generated, the signal to be visualized can be selected via the **slider**.''')

        # select and compare signals
        i_signal = st.slider('Signal number', 1, V.shape[0]) - 1 if V.shape[0] > 1 else 0
        cls._st_compare_individual_signals(V[i_signal], R[i_signal])

    @classmethod
    def st_plot_partial_reconstructions(cls, V: np.ndarray, nmf: TransformInvariantNMF, verbose: bool = True):
        """
        Visualizes the partial reconstructions of the given input by the different NMF atoms.

        Parameters
        ----------
        V : np.ndarray
            The input that was factorized via NMF.
        nmf : TransformInvariantNMF
            The trained NMF object.
        verbose : bool
            If True, show detailed information.
        """
        st.markdown('# Partial signal reconstructions')

        # show explanatory text
        if verbose:
            st.caption('''The visualization below shows the **learned dictionary atoms (left) and their partial contributions
            (right)** to the reconstruction of an individual signal. If more than one input signal has been generated, the
            signal to be visualized can be selected via the **slider**.''')

        # select the signal and show the partial reconstruction
        i_signal = st.slider('Signal number', 1, V.shape[0], key='i_signal_partial') - 1 if V.shape[0] > 1 else 0
        for i_atom in range(nmf.n_atoms):
            R_atom = nmf.R_partial(i_atom)
            cols = st.columns(2)
            for col, signals, signal_opts, opts in zip(
                    cols,
                    [[nmf.W[i_atom]], [R_atom[i_signal], V[i_signal]]],
                    [[{}], [{'label': 'Atom contribution', 'color': 'tab:red', 'linestyle': '--'}, {'label': 'Signal'}]],
                    [{'title': f'Atom {i_atom + 1}'}, {'title': 'Atom contribution'}],
            ):
                with col:
                    cls.plot_signals(signals, signal_opts, opts)

    @classmethod
    def plot_signals(
            cls,
            signals: List[np.ndarray],
            signal_opts: Optional[Iterable[dict]] = None,
            opts: Optional[dict] = None,
    ):
        """Wrapper for `_plot_signals` to fill the default arguments."""
        if signal_opts is None:
            signal_opts = repeat({})
        if opts is None:
            opts = {}
        cls._plot_signals(signals, signal_opts, opts)

    @classmethod
    @abstractmethod
    def st_define_signal_params(cls, verbose: bool = True) -> dict:
        """
        Defines all signal parameters via streamlit widgets and returns them in a dictionary.

        Parameters
        ----------
        verbose : bool
            If True, show detailed information.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def generate_signal(cls, signal_params: dict) -> Tuple[np.ndarray, np.ndarray]:
        """Creates a single signal using the specified signal parameters. Returns the signal and the used NMF atoms."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def _st_compare_individual_signals(cls, V_i: np.ndarray, R_i: np.ndarray):
        """
        Compares a single signal and its reconstruction in streamlit.

        Parameters
        ----------
        V_i : np.ndarray
            A single input signal from the input that was factorized via NMF.
        R_i : np.ndarray
            The NMF reconstruction of the given input signal.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def _plot_signals(cls, signals: List[np.ndarray], signal_opts: Iterable[dict], opts: dict):
        """
        Visualizes a given list of signals.

        Parameters
        ----------
        signals : List[np.ndarray]
            The list of signals to be plotted.
        signal_opts : Iterable[dict]
            A list of dictionaries containing plotting options for each individual signal.
        opts : dict
            A dictionary containing global plotting options.
        """
        raise NotImplementedError


class SignalTool1D(SignalTool):
    """A utility class to handle 1-D multi-channel signals (time series data)."""

    @classmethod
    def st_define_signal_params(cls, verbose: bool = True) -> dict:

        # define the number of channels
        n_channels = st.sidebar.number_input('# Channels', min_value=1, value=3, max_value=5, help=HELP_CHANNEL)
        explanation(HELP_CHANNEL, verbose)

        # define the pulse shapes
        help_shapes = \
            '''The **pulse shapes** that can be combined along different channels to form a multi-channel time-series
            symbol.'''
        shapes = st.sidebar.multiselect('Pulse shapes', ['n', '-', '^', 'v', '_'], ['n', '-', '^', 'v', '_'], help=help_shapes)
        explanation(help_shapes, verbose)

        # to avoid having too many different symbols, consider only those where all channels are identical
        help_symbols = \
            '''The **set of symbols** that form the atom dictionary of of multi-channel time series symbols for
             signal generation. The subset of channel-symmetric symbols is pre-selected.'''
        symbols = st.sidebar.multiselect('Symbols', [''.join(chars) for chars in product(*repeat(shapes, n_channels))],
                                         [s * n_channels for s in shapes], help=help_symbols)
        explanation(help_symbols, verbose)

        # define the number of pulses
        help_n_pulses = 'The **number of symbols** concatenated randomly to form a signal.'
        n_pulses = st.sidebar.number_input('# Symbols', min_value=1, value=3, help=help_n_pulses)
        explanation(help_n_pulses, verbose)

        # define the pulse length
        help_pulse_length = 'The **length** of each individual multi-channel symbol.'
        pulse_length = st.sidebar.number_input('Symbol length', min_value=1, value=20, help=help_pulse_length)
        explanation(help_pulse_length, verbose)

        # create the parameter dictionary
        signal_params = dict(
            n_pulses=n_pulses,
            symbols=symbols,
            pulse_length=pulse_length,
        )

        return signal_params

    @classmethod
    def generate_signal(cls, signal_params: dict) -> Tuple[np.ndarray, np.ndarray]:
        signal, W = generate_pulse_train(**signal_params)
        return signal, W

    @classmethod
    def _st_compare_individual_signals(cls, V_i: np.ndarray, R_i: np.ndarray):
        signals = [V_i, R_i]
        opts = [{'label': 'Reconstruction', 'color': 'tab:red', 'linestyle': '--'}, {'label': 'Signal', 'zorder': -1}]
        cls.plot_signals(signals, opts)

    @classmethod
    def _plot_signals(cls, signals: List[np.ndarray], signal_opts: Iterable[dict], opts: dict):
        assert len(np.unique([signal.shape[0] for signal in signals])) == 1
        n_channels = signals[0].shape[0]
        with plt.style.context('seaborn'):
            fig, axs = plt.subplots(nrows=n_channels)
            axs = np.atleast_1d(axs)
            for signal, signal_opt in zip(signals, signal_opts):
                for i_channel, ax in enumerate(axs):
                    ax.plot(signal[i_channel], **signal_opt)
            plt.legend()
            fig.suptitle(opts.get('title'))
            st.pyplot(fig)


class SignalTool2D(SignalTool):
    """A utility class to handle 2-D multi-channel signals (image data)."""

    @classmethod
    def st_define_signal_params(cls, verbose: bool = True) -> dict:

        # choose between grayscale or color images
        n_channels = st.sidebar.radio('# Channels', ['1 (Grayscale images)', '3 (Color images)'], 0, help=HELP_CHANNEL)
        n_channels = 1 if n_channels == '1 (Grayscale images)' else 3
        explanation(HELP_CHANNEL, verbose)

        # create all possible combinations of shapes and color
        shapes = ['+', 'x', 's']
        colors = ['r', 'g', 'b', 'y', 'm', 'c', 'w'] if n_channels == 3 else ['']
        all_symbols = [''.join(spec) for spec in product(shapes, colors)]

        # select the symbols to be used
        help_symbols = \
            '''The **set of symbols** that form the atom dictionary of image patches for signal generation. The first
            character defines the visual shape of the corresponding symbol. The second character (only available for color
            images) defines the color of the symbol. For color images, a representative subset of symbols is pre-selected.'''
        symbols = st.sidebar.multiselect('Symbols', all_symbols, ['+r', 'xg', 'sb'] if n_channels == 3 else all_symbols,
                                         help=help_symbols)
        explanation(help_symbols, verbose)

        # select the number of symbols per dimension
        help_n_symbols = \
            '''The **number of symbols** placed randomly next to each other both horizontally and vertically to generate an
            input image.'''
        n_symbols = st.sidebar.number_input('# Symbols per dimension', min_value=1, value=5, help=help_n_symbols)
        explanation(help_n_symbols, verbose)

        # define the size of each symbol
        help_symbol_size = 'The **size of each symbol** in pixels per dimension. All symbols are of square size.'
        symbol_size = st.sidebar.number_input('Symbol size', min_value=1, value=10, help=help_symbol_size)
        explanation(help_symbol_size, verbose)

        # create the parameter dictionary
        signal_params = dict(
            n_symbols=n_symbols,
            symbol_size=symbol_size,
            symbols=symbols,
        )

        return signal_params

    @classmethod
    def generate_signal(cls, signal_params: dict) -> Tuple[np.ndarray, np.ndarray]:
        signal, W = generate_block_image(**signal_params)
        return signal, W

    @classmethod
    def _st_compare_individual_signals(cls, V_i: np.ndarray, R_i: np.ndarray):
        cols = st.columns(2)
        for col, X, title in zip(cols, [V_i, R_i], ['Input', 'Reconstruction']):
            with col:
                cls.plot_signals([X], opts={'title': title})

    @classmethod
    def _plot_signals(cls, signals: List[np.ndarray], signal_opts: Iterable[dict], opts: dict):
        fig = plt.figure()
        plt.imshow(signals[0].transpose((1, 2, 0)) / signals[0].max())
        plt.title(opts.get('title'))
        st.pyplot(fig)


# TODO: replace st.cache with st.memo + remove deepcopies when called
# currently this is not possible because the experimental memo function fails at hashing MiniBatchAlgorithm Enum instances
@st.cache(hash_funcs={DeltaGenerator: lambda _: None}, allow_output_mutation=True)
def fit_nmf_model(V, nmf_params, fit_params, progress_bar):
    nmf = TransformInvariantNMF(**nmf_params)
    n_steps = fit_params['n_iterations'] if 'n_iterations' in fit_params else fit_params['n_epochs']
    nmf.fit(V, progress_callback=lambda _, x: progress_bar.progress((x + 1) / n_steps), **fit_params)
    return nmf
