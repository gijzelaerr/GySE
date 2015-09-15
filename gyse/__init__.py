import argparse
from casacore.tables import table
import numpy as np
import cv2


def open_image(path):
    t = table(path, ack=False)
    return t[0]['map'][0][0]


def main():
    parser = argparse.ArgumentParser(description='Locate sources in an image')
    parser.add_argument('image', type=str, help='image')

    args = parser.parse_args()
    map = open_image(args.image)


    # create a blurred version to get an idea of the RMS in the image
    blur = cv2.blur(map, ksize=(50, 50))

    # substract the blurred image from the image to remove noise
    clean = map - blur

    # threshold image to remove non zero values
    retval, thresh = cv2.threshold(clean, 0, maxval=255, type=cv2.THRESH_TOZERO)

    # scale image to max 255
    max_ = clean.max()
    scale_factor = 255 / max_
    scaled = thresh * scale_factor

    # blob detect only works with inversed 8 bit single channel imges
    inverse = 255 - scaled
    downscale = inverse.astype(np.uint8)

    # Detect blobs.
    detector = cv2.SimpleBlobDetector()
    keypoints = detector.detect(downscale)

    overlay = cv2.drawKeypoints(scaled.astype(np.uint8), keypoints,
                                color=(0, 0, 255),  flags=4)  # cv2.DRAW_RICH_KEYPOINTS


    while True:
        cv2.imshow('map', overlay)

        if 0xFF & cv2.waitKey(5) == 27:
            break

    cv2.destroyAllWindows()
