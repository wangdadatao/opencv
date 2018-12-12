"""
ROI区域(region of interest): 感兴趣区域

"""

import cv2 as cv
import numpy as np


def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_img", copyImg)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (100, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("mask", mask)


img = cv.imread("car.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)

fill_color_demo(img)
# fill_binary()

car = img[50:250, 100:300]
car = cv.cvtColor(car, cv.COLOR_BGR2GRAY)
cv.imshow("car", car)

cv.waitKey(0)
