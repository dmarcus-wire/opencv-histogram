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

DATA_PRE_PROCESSING

PROCESSING
- instantiate CLAHE
- pass in tilextile and clips
- apply 