# USAGE
# python simple-equal.py -i ../moon.jpg

# import packages
import argparse
import cv2

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to the input image")
args = vars(ap.parse_args())

# load the image from disk
# convert to grayscale
print("[INFO] loading input image")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
print("[INFO] performing histogram equalization")
equalized = cv2.equalizeHist(gray)

# show original grayscale and equalized
cv2.imshow("Input", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)