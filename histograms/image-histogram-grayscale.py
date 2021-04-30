# USAGE
# python grayscale_histogram.py --image ../images/madison.jpg

# import the necessary packages
from matplotlib import pyplot as plt
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute a grayscale histogram
# pass in [image] as a list, compute histogram for [0] channel =gray, None =mask, 256 bins, 0-256 possible pixel values
# x-axis 0-256, y-axis count of pixels
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# matplotlib expects RGB images so convert and then display the image
# with matplotlib
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

# plot the histogram = raw pixel intensities...256*256 binned pixels
plt.figure()
plt.title("Grayscale Histogram")
# plot x-axis the Bins
plt.xlabel("Bins")
# plot y-axis the pixels
plt.ylabel("# of Pixels")
plt.plot(hist)
# limit values 0 to 256
plt.xlim([0, 256])

# normalize the histogram...sum all pixels values and divide each bin by that sum
# 256*256=65536..divide each by that value
# therefore all  bin values add up to 1...normalized histogram
# this supports images of different sizes to compare distances between histograms
hist /= hist.sum()

# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()