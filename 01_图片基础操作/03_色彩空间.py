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


def extract_object():
    capture = cv.VideoCapture("football.mp4")

    while (True):
        ret, frame = capture.read()
        if not ret:
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lower_hsv = np.array([78, 43, 46])
        upper_hsv = np.array([99, 255, 255])

        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)

        cv.imshow("football", frame)
        cv.imshow("mask", mask)

        c = cv.waitKey(40)
        if c == 27:
            break

    return


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)

    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)

    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)


img = cv.imread("car.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)

b, g, r = cv.split(img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

img[:, :, 0] = 0
cv.imshow("img", img)

# color_space_demo(img)
# extract_object()

cv.waitKey(0)
