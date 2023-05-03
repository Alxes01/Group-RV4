# Getting the correct coordination reference for RoboDK
import cv2 as cv
import numpy as np
import os

def match(path):
    # Reading in grayscale the corrected and reference image for alignment and RoboDK reference
    img = cv.imread(os.path.join(path,"Corrected.png"))
    imgqr = cv.imread(os.path.join(path,"QR.png"))

    # Resizing the QR image
    scale_percent = 30 # percent of original size
    width = int(imgqr.shape[1] * scale_percent / 100)
    height = int(imgqr.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    imgqr = cv.resize(imgqr, dim, interpolation=cv.INTER_AREA)

    #cv.imwrite("QRsize.jpg", imgqr)

    # Converting images to grayscale
    img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img2 = cv.cvtColor(imgqr, cv.COLOR_BGR2GRAY)

    # Detecting ORB features
    orb = cv.ORB_create(3200)
    key1, desc1 = orb.detectAndCompute(img1, None)
    key2, desc2 = orb.detectAndCompute(img2, None)

    # Matching features
    bf = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    #bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1,desc2, None)

    # Sorting matches by score (precision) - Different interpretation
    # matches.sort(key=lambda x: x.distance, reverse=False)
    # matches = tuple(sorted(matches, key=lambda x: x.distance))
    list(matches).sort(key=lambda x: x.distance, reverse=False)

    # Choosing only good matches (top x%)
    matches = matches[: int(len(matches) * 0.04)]
    num_matches = len(matches)

    # Save chosen matches
    imgmat = cv.drawMatches(img, key1, imgqr, key2, matches, None)
    cv.imwrite(os.path.join(path, "Matches.png"), imgmat)

    # Creating empty arrays
    p1 = np.zeros((num_matches, 2))
    p2 = np.zeros((num_matches, 2))

    for i in range(len(matches)):
        p1[i, :] = key1[matches[i].queryIdx].pt
        p2[i, :] = key2[matches[i].trainIdx].pt

    # Finding the homography
    homography, mask = cv.findHomography(p1, p2, cv.RANSAC)

    # Transforming the original image to match the reference and saving it
    height, width, channels = imgqr.shape
    matched_img = cv.warpPerspective(img, homography, (width, height))
    cv.imwrite(os.path.join(path, "Matched.png"), matched_img)

    print("Matching complete")
