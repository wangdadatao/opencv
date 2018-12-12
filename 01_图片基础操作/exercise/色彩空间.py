'''
常见色彩空间：
1 RGB
2 HSV
    h: 0 -- 100
    s: 0 -- 255
    v; 0 --255
3 HIS
4 YCrCb
5 YUV
'''
import cv2 as cv
import numpy as np


def extract_img(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([35, 43, 46])
    upper_hsv = np.array([77, 255, 255])

    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)

    cv.imshow("mask", mask)

    c = cv.waitKey(40)


def extract_object():
    capture = cv.VideoCapture("hua.mp4")

    while (True):
        ret, frame = capture.read()
        if not ret:
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_hsv = np.array([0, 43, 46])
        upper_hsv = np.array([10, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow("football", frame)
        cv.imshow("mask", dst)

        c = cv.waitKey(40)
        if c == 27:
            break

    return


# extract_img(img)
extract_object()

cv.waitKey(0)
