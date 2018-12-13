"""
灰度直方图：
    统计每个像素灰度出现的概率
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def grayHist(image):
    (h, w, ch) = image.shape
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
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

    x = np.linspace(0, 255, 256)
    y = count
    plt.bar(x, y, 0.9, alpha=1, color='b')
    plt.show()


img = cv.imread("../imgs/apple.jpg", 1)
# cv.imshow("img", img)

grayHist(img)

# cv.waitKey(0)
cv.destroyAllWindows()
