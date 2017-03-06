"""Contains the functions for implementing img2svd."""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread


def get_svd_from_grayscale_image(imgpath, sigma_coverage_percentage=95, plot=True):
    """Returns the compressed U, S and V.H after SVD of the image.

    The image is first converted to grayscale and then `n_components` (similar to
    principal components) are chosen based on the `sigma_coverage_percentage`.

    We choose the first `n_components` such that:
    `(np.sum(sigma[:n_components]) / np.sum(sigma)) >= (sigma_coverage_percentage / 100)`

    Args:
        imgpath (str): The full path of the image.
        sigma_coverage_percentage (int, float): It is an estimate of how much information
            should be preserved. It is used to calculate `n_components` as described above.
        plot (bool): Whether to plot the original vs reconstructed/compressd image.

    Returns:
        U, S, V_H (tuple of ndarrays): The same as the output of `np.linalg.svd`, however
            instead of the full U, S, V_H returned by the `np.linalg.svd` we return only
            `U[:, :n_components], S[:n_components], V_H[:n_components, :]` where `n_components`
            is computed as described above.

            The `n_components` is the same as U.shape[1] or S.shape[0] or V_H.shape[0].
    """
    imgarr = imread(imgpath, as_grey=True)
    u, s, v = np.linalg.svd(imgarr, full_matrices=True)  # s is already sorted
    # The number of components required to have the sigma_coverage_percentage. +1 is for index.
    n_components = np.argmax((np.cumsum(s) / np.sum(s)) >= (sigma_coverage_percentage / 100.0)) + 1

    if plot is True:
        s_dot_v = np.dot(np.diag(s[:n_components]), v[:n_components, :])
        u_dot_s_dot_v = np.dot(u[:, :n_components], s_dot_v)
        imgarr_reconstructed = u_dot_s_dot_v
        figure, axes = plt.subplots(2, sharex=False)
        axes[0].imshow(imgarr, cmap='Greys_r')
        axes[1].imshow(imgarr_reconstructed, cmap='Greys_r')
        plt.show()

    return u[:, :n_components], s[:n_components], v[:n_components, :]
