# Color recognition and lego brick position
import cv2 as cv
import numpy as np
import os
import math


def recognititiona(path):

    # Upper and lower boundaries of colours
    # https://i.stack.imgur.com/gyuw4.png
    # white (purple in this case), orange, yellow, green, blue
    lbound = np.array([[120, 150, 70],
                      [0, 150, 70],
                      [11, 120, 70],
                      [30, 80, 50],
                      [100, 150, 60]])

    ubound = np.array([[170, 255, 255],
                      [10, 255, 255],
                      [25, 255, 255],
                      [100, 255, 255],
                      [150, 255, 255]])
    # Importing and defining the picture taken by camera
    imgc = cv.imread(os.path.join(path, "Matched.png"))

    # Converting initial image to HSV
    imghsv = cv.cvtColor(imgc, cv.COLOR_BGR2HSV)
    cv.imwrite(os.path.join(path, "HSV.png"), imghsv)

    # Kernel definition
    kernel = np.ones((10, 10), np.uint8)

    # Creating an array for important parameters to store
    # [x, y, z, rotation, colour, assigned] (for future use)
    par = np.array([[0, 0, 0, 0, 0]])

    # Choosing only given colour
    for i in range(5):
        # Cycling through all the colours and saving them into separate images
        c = cv.inRange(imghsv, lbound[i], ubound[i])
        ck1 = cv.morphologyEx(c, cv.MORPH_OPEN, kernel)
        ck2 = cv.morphologyEx(ck1, cv.MORPH_CLOSE, kernel)

        # Saving the image to folder
        cv.imwrite(os.path.join(path, "Colour_{}.png".format(i)), ck2)

        # Creating a copy of Isolated Blocks.png
        # contimg = cv.cvtColor(ck2, cv.COLOR_BGR2GRAY)

        # Finding all contours of the lego bricks
        contours, hierarchy = cv.findContours(ck2, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        for j, cnt in enumerate(contours):

            # Ignoring object which are small or too large
            area = cv.contourArea(cnt)
            if area < 1000 or 100000000 < area:
                continue

            # minArea returns the (center(x, y), (width, height), angle of rotation)
            rect = cv.minAreaRect(cnt)
            box = cv.boxPoints(rect)
            box = np.intp(box)

            angle = int(rect[2])

            # Converting angles to correct angles
            angle = angle - 90

            # Displaying relevant parameters on the image
            label = "Rotation angle:" + str(angle) + "degrees"
            cv.putText(imgc, label, (int(rect[0][0]), int(rect[0][1])),
                    cv.FONT_HERSHEY_SIMPLEX, 0.7, (180, 180, 180), 1, cv.LINE_AA)
            cv.drawContours(imgc, [box], 0, (180, 180, 180), 2)

            # Saving the image with displayed parameters
            cv.imwrite(os.path.join(path, "Contours and Angles.png"), imgc)

            # Storing all parameters into one array
            # [x, y, z, rotation, colour, number of figures] (for future use) - Pixel to mm, 0.28 and 0.26 worked best
            par1 = np.array([[int(rect[0][0] * 0.28),
                         int(rect[0][1] * 0.26),
                         0,
                         angle,
                         (i + 1)]])

            # Combining arrays
            par = np.append(par, par1, axis=0)

    # Delete the first filler row of 0s
    pard = np.delete(par, 0, 0)
    print("Recognition complete")
    return pard