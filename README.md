# Multi-frame Noise Reduction
Reduce an image stack taken in short succession into a single image with reduced noise. The image stack is not assumed to be perfectly aligned but should roughly show the same scene. Optical flow is tried as a registration and alignment method, using the disparity map to assemble the corresponding pixels between the images to perform filtering on.

# ToDo
[] Establish Framework (ArgParse, IO)
[] Implement Median Filtering kernel
[] SetUp Testing Framework
[] *Milestone 1* MFNR without registration and alignment
[] Read FlowNet Paper
[] Acquire Training Data
[] Train Keras FlowNet
[] Use FlowNet for Optical Flow computation
[] *Milestone 2* robust MFNR on handheld images
