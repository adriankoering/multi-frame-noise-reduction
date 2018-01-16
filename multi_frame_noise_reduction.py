import cupy as cp
import matplotlib.pyplot as plt
from skimage import io


def load_image_stack(*files):
    """
    Given a list of filenames, open each image file.
    The image is then converted into a cupy array of
    shape (N, H, W, C) where N == len(files).
    """
    return cp.array([cp.array(io.imread(f) for f in files])

def optical_flow(img_stack):
    """
    Given an image stack (N, H, W, C) calculate the optical flow
    beginning from the center image (rounded down) towards either
    end.

    Returns the disparity maps stackes as (N, H, W, 2)
    """
    pass

def median_filtering(img_stack, disparity_stack):
    """
    Given an image stack (N, H, W, C) and a disparity stack
    start with a pixel (x, y) in the center image of the stack
    (rounded down) and follow the disparity in the corresponding
    maps to assemble an vector of pixels through the first dimension.

    Return the image with the median color of each vector in each pixel.
    """
    return img_stack.median(axis=0)


if __name__ == "__main__":
    pass
    # Argparse
    # img_stack = load_image_stack(args.files)
    # dis_stack = optical_flow(img_stack)
    # out_image = median_filtering(img_stack, dis_stack)
