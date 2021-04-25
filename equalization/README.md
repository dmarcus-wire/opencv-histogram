Applying histogram equalization starts by computing the histogram of pixel intensities in an input grayscale/single-channel image:
With histogram equalization, our goal is to spread these pixels to buckets that don’t have as many pixels binned to them.
Mathematically, what this means is that we’re attempting to apply a linear trend to our cumulative distribution function (CDF

simple_equalization.py
- Performs basic histogram equalization using OpenCV’s cv2.equalizeHist function
- boost contrast (with noise)

SETUP
- import packages  
- path to image

DATA_PRE_PROCESSING  
- load image
- convert to grayscale (single channel)

PROCESSING
- magic


adaptive_equalization.py
- Uses OpenCV’s cv2.createCLAHE method to perform adaptive histogram equalization
- boost contrast (without noise)
- slices image up and applies

SETUP
- import packages  
- path to image

DATA_PRE_PROCESSING  
- load image
- convert to grayscale (single channel)

PROCESSING
- instantiate CLAHE
- pass in tilextile and clips
- apply 