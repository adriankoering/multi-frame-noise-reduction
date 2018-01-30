import numpy as np

def median_filtering(img_stack, disparity_stack):
    """
    Given an image stack (N, H, W, C) and a disparity stack
    start with a pixel (x, y) in the center image of the stack
    (rounded down) and follow the disparity in the corresponding
    maps to assemble an vector of pixels through the first dimension.

    Return the image with the median color of each vector in each pixel.
    """
    return img_stack.median(axis=0)
