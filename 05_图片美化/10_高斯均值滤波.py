"""
高斯滤波
均值滤波
"""

import cv2 as cv
import numpy as np


def gaussianAverage(image):
    # 高斯滤波
    gaussian = cv.GaussianBlur(image, (5, 5), 1.5)
    cv.imshow("高斯滤波", gaussian)

    # 均值滤波
    (h, w, ch) = image.shape
    aveImg = np.zeros((h, w, 3), np.uint8)
    
    for i in range(3, h - 3):
        for j in range(3, w - 3):
            subB = int(0)
            subG = int(0)
            subR = int(0)
            for m in range(-3, 3):
                for n in range(-3, 3):
                    (b, g, r) = image[i + m, j + n]
                    subB = subB + int(b)
                    subG = subG + int(g)
                    subR = subR + int(r)
            b = np.uint8(subB / 36)
            g = np.uint8(subG / 36)
            r = np.uint8(subR / 36)
            aveImg[i, j] = (b, g, r)

    cv.imshow("均值滤波", aveImg)


img = cv.imread("../imgs/apple.jpg", 1)
cv.imshow("img", img)
gaussianAverage(img)

cv.waitKey(0)
cv.destroyAllWindows()
