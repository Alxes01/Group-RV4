# # Capturing the image
import cv2 as cv
import os

def capture(path):
    # First a connection to the camera has to made, where a cap on the data stream is set.
    videoCaptureObject = cv.VideoCapture(1, cv.CAP_DSHOW)

    # Then the dimensions for the picture is set
    videoCaptureObject.set(3, 1920)  # width=1920
    videoCaptureObject.set(4, 1080)  # height=1080

    # Then the data from the camera is read, and a picture is taken.
    ret, frame = videoCaptureObject.read()

    # Then the picture is saved in the pictures folder, with the input path set in the main script.
    cv.imwrite(os.path.join(path, 'Camera.png'), frame)

    # Then the connection to the camera is broken
    videoCaptureObject.release()

    return print("Photo done")

