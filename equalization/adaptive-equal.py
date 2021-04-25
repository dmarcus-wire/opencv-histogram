# USAGE
# python adaptive-equal.py -i ../moon.jpg

# import packages
import argparse
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, required=True,
                help="path to input image")
ap.add_argument("-c","--clip", type=float, default=2.0,
                help="threshold for contrast limiting")
ap.add_argument("-t", "--tile", type=int, default=8,
                help="tile grid size; divides image into tile x tile cells")
args = vars(ap.parse_args())

# load the input image from disk
print("[INFO] loading input image")
image = cv2.imread(args["image"])
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply CLAHE (contrast limited adaptive histogram equalization)
print("[INFO] applying CLAHE")
clahe = cv2.createCLAHE(clipLimit=args["clip"],
                        tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)

# show original image
cv2.imshow("Input", gray)
# show CLAHE image
cv2.imshow("CLAHE", equalized)
# wait to close
cv2.waitKey(0)