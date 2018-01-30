import numpy as np
from skimage import io


def load_image_stack(*files):
    """
    Given a list of filenames, open each image file.
    The image is then converted into a cupy array of
    shape (N, H, W, C) where N == len(files).
    """
    return np.array([np.array(io.imread(f)) for f in files])
