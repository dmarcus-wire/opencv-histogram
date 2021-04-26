# USAGE
# python color-correction.py -r reference.jpg -i 01.jpg

# why adjust lighting conditions? why do color correction?
# consistent standardized lighting and lighting across the entire shoot
# if you want the color to look the same
# color perception can skew the original image color (i.e. hued)
# image processing pipelines against a gold-standard image

# import packages
from imutils.perspective import four_point_transform # topdown birds-eye view
from skimage import exposure # color matching
import numpy as np # numerical array parsing
import argparse
import imutils
import cv2
import sys # gracefully exit script

def find_color_card(image):
    # load ArUCo dictionary based on the CORRECT dictionary
    # grab the ArUCo parameters
    # detect the markers in the input image
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    arucoParams = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

    #try to extract the coordinates of the color correction
    try:
        # otherwise, we've found the found ArUco markers
        # continue flattening the ArUco IDs to 1D array
        ids = ids.flatten()

        # extract the top-left marker
        # where is the id 923
        i = np.squeeze(np.where(ids == 923))
        # lookup index to get marker with 923
        topLeft = np.squeeze(corners[i])[0]

        # extract the top-right marker
        i = np.squeeze(np.where(ids == 1001))
        topRight = np.squeeze(corners[i])[1]

        # extract the bottom-right marker
        i = np.squeeze(np.where(ids == 241))
        bottomRight = np.squeeze(corners[i])[2]

        # extract the bottom-left marker
        i = np.squeeze(np.where(ids == 1007))
        bottomLeft = np.squeeze(corners[i])[3]

    # we could not find the color correction card, so gracefully return
    except:
        return None

    # build list of reference points and apply perspective
    # transform to obtain top-down, birds-eye view of the color matching card
    cardCoords = np.array([topLeft, topRight,
                           bottomRight, bottomLeft])
    # topdown view comes in here
    card = four_point_transform(image, cardCoords)

    # construct the argument parser
    ap = argparse.ArgumentParser()
    ap.add_argument("-r", "--reference", required=True,
                    help="path to the input reference image")
    ap.add_argument("-i","--image", required=True,
                    help="path to the input image to apply color correction")
    args = vars(ap.parse_args())

    # load the reference image from disk
    print("[INFO] loading images...")
    ref = cv2.imread(args["reference"])
    image = cv2.imread(args["input"])

    # resize the reference input images
    ref = imutils.resize(ref, width=600)
    image = imutils.resize(image, width=600)

    # display refernce and input images on screen
    cv2.imshow("Reference", ref)
    cv2.imshow("Input", ref)

    # find the color matching card in each image
    print("[INFO] finding color matching cards...")
    refCard = find_color_card(ref)
    imageCard = find_color_card(image)

    # if the color matching card is not found in reference
    # or input images, gracefully exit
    if refCard is None or imageCard is None:
        print("[INFO] could not find color matching card in both images")
        sys.exit(0)

    # show the color matching card in the reference image and input image
    cv2.imshow("Reference Color Card", refCard)
    cv2.imshow("Input Color  Card", refCard)

    # apply histogram matching from the color matching card
    # in the ref image to the color matching card in the input image
    print("[INFO] matching images...")
    imageCard = exposure.match_histograms(imageCard, refCard,
                                          multichannel=True)

    # show input color matching card after histogram matching
    cv2.imshow("Input Color Card After Matching", imageCard)
    cv2.waitKey(0)