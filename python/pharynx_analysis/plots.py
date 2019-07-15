import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def plot_individual_profile_data_by_strain_and_pair(profile_data, cmin, cmax, cmap_name, linewidth=1, ylim=None,
                                                    alpha=1, figsize=None, cmap_boundary_trim=0):
    """
    TODO: Documentation
    Parameters
    ----------
    profile_data
    cmin
    cmax
    cmap_name
    linewidth
    ylim
    alpha
    figsize
    cmap_boundary_trim

    Returns
    -------

    """
    cmap = cm.get_cmap(name=cmap_name)
    norm = matplotlib.colors.Normalize(vmin=cmin, vmax=cmax)

    strains = np.unique(profile_data.strain.data)

    if ylim is None:
        ylim = [profile_data.min(), profile_data.max()]

    n_strains = len(strains)
    fig, axes = plt.subplots(n_strains, 2, figsize=figsize)

    for strain, ax in zip(strains, axes):
        for i in range(2):
            data = profile_data.isel(pair=i).sel(strain=strain)
            color_data = data[:, cmap_boundary_trim:profile_data.position.size - cmap_boundary_trim]
            means_normed = norm(color_data.mean(dim='position').data)
            colors = cmap(means_normed)
            colors[:, 3] = alpha
            for animal_idx in range(data.shape[0]):
                ax[i].plot(data[animal_idx], c=colors[animal_idx], linewidth=linewidth)
                ax[i].set_ylim(ylim)
            ax[i].set_title(f'{strain} (Pair {i})')
            if cmap_boundary_trim > 0:
                boundary_line_args = {
                    'color': 'k', 'linewidth': 1, 'alpha': 0.1,
                    'linestyle': '--'

                }
                ax[i].axvline(cmap_boundary_trim, **boundary_line_args)
                ax[i].axvline(profile_data.position.size - cmap_boundary_trim, **boundary_line_args)

    plt.tight_layout()


def plot_average_by_strain_and_pair(data):
    for strain in np.unique(data.strain):
        for pair in data.pair.data:
            data_subset = data.sel(strain=strain, pair=pair)