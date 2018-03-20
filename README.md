![License:MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)
[![Build Status](https://travis-ci.org/adriankoering/multi-frame-noise-reduction.svg?branch=master)](https://travis-ci.org/adriankoering/multi-frame-noise-reduction)


# Multi-frame Noise Reduction
Reduce an image stack taken in short succession into a single image with reduced noise. The image stack is not assumed to be perfectly aligned but should roughly show the same scene. Optical flow is tried as a registration and alignment method, using the disparity map to assemble the corresponding pixels between the images to perform filtering on.


## WIP
