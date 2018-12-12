import cv2 as cv
import numpy as np

"""
灰色图像颜色反转
色彩图像颜色反转
"""


# 灰度图片颜色反转
def gray_re(image):
    h, w, ch = image.shape
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    dst = np.zeros((h, w, 1), np.uint8)

    for i in range(0, h):
        for j in range(0, w):
            grayPixel = gray[i, j]
            dst[i, j] = 255 - grayPixel
    cv.imshow("gray_re", dst)


# 色彩图像颜色反转
def rgb_re(image):
    h, w, ch = image.shape
    dst = np.zeros([h, w, 3], np.uint8)

    for i in range(0, h):
        for j in range(0, w):
            grayPixel = image[i, j]
            dst[i, j] = 255 - grayPixel
    cv.imshow("gray_re", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

rgb_re(img)

cv.waitKey(0)
cv.destroyAllWindows()
