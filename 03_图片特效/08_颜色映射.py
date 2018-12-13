"""
颜色映射表：
"""
import math
import cv2 as cv
import numpy as np


def rgbMap(image):
    (h, w, ch) = image.shape
    dst = np.zeros((h, w, 3), np.uint8)
    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            b = 255 if b * 1.5 > 255 else b * 1.5
            g = 255 if g * 1.3 > 255 else g * 1.3

            dst[i, j] = (b, g, r)

    cv.imshow("rgb_map", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

rgbMap(img)

cv.waitKey(0)
cv.destroyAllWindows()
