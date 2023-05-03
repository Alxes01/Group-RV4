# Applying the calibration
import cv2 as cv
import numpy as np
import os


def correction(path):
    # Reading the captured image
    imgc = cv.imread(os.path.join(path, "Camera.png"))

    # Inputting the results of camera calibration
    cameramat = np.array([[1429.59689, 0, 930.342294],
                          [0, 1430.03433, 552.460564],
                          [0, 0, 1]])

    distcoef = np.array([0.0358131336238750, -0.149379521755432, 0, 0, 0])

    # Applying the calibration to captured image
    imgu = cv.undistort(imgc, cameramat, distcoef)

    # Saving the corrected image
    cv.imwrite(os.path.join(path, "Corrected.png"), imgu)

    return print("Correction complete")
