"""
彩色直方图：
    统计每个像素各通道颜色出现的次数/概率
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def imageHist(image):
    (h, w, ch) = image.shape
    countB = np.zeros(256, np.float)
    countG = np.zeros(256, np.float)
    countR = np.zeros(256, np.float)

    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            indexB = int(b)
            indexG = int(g)
            indexR = int(r)
            countB[indexB] = countB[indexB] + 1
            countG[indexG] = countG[indexG] + 1
            countR[indexR] = countR[indexR] + 1

    # 计算概率
    allPixel = h * w
    for i in range(0, 256):
        countB[i] = countB[i] / allPixel
        countG[i] = countG[i] / allPixel
        countR[i] = countR[i] / allPixel

    x = np.linspace(0, 255, 256)

    plt.bar(x, countB, 0.9, alpha=1, color='b')
    plt.show()

    plt.bar(x, countG, 0.9, alpha=1, color='g')
    plt.show()

    plt.bar(x, countR, 0.9, alpha=1, color='r')
    plt.show()


img = cv.imread("../imgs/1.jpg", 1)
# cv.imshow("img", img)

imageHist(img)

# cv.waitKey(0)
cv.destroyAllWindows()
