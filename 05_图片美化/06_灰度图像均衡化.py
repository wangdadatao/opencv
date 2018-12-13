"""
累积概率

"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def grayHistEqualize(image):
    (h, w, ch) = image.shape
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)

    count = np.zeros(256, np.float)

    for i in range(h):
        for j in range(w):
            pixel = gray[i, j]
            index = int(pixel)
            count[index] = count[index] + 1

    # 计算概率
    allPixel = h * w
    for i in range(255):
        count[i] = count[i] / allPixel

    # 计算累积概率
    sum = float(0)
    for i in range(0, 256):
        sum = sum + count[i]
        count[i] = sum

    # 计算映射表
    map = np.zeros(256, np.uint16)
    for i in range(0, 256):
        map[i] = np.uint16(count[i] * 255)

    # 映射
    for i in range(0, h):
        for j in range(0, w):
            pixel = gray[i, j]
            gray[i, j] = map[pixel]
    cv.imshow("dst_img", gray)


img = cv.imread("../imgs/apple.jpg", 1)
# cv.imshow("img", img)

grayHistEqualize(img)

cv.waitKey(0)
cv.destroyAllWindows()
