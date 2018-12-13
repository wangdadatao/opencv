"""
浮雕效果：
相邻像素的灰度值之差加上一个固定值
    加固定值：增强浮雕的灰度等级
    相邻像素差：为了增强边缘特征
"""
import math
import cv2 as cv
import numpy as np


def embossmentEffect(image):
    (h, w, ch) = image.shape
    dst = np.zeros((h, w, 1), np.uint8)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    for i in range(0, h):
        for j in range(0, w - 1):
            grayP0 = int(gray[i, j])
            grayP1 = int(gray[i, j + 1])
            newP = grayP0 - grayP1 + 150
            if newP > 255:
                newP = 255
            if newP < 0:
                newP = 0
            dst[i, j] = newP

    cv.imshow("embossment_effect", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

embossmentEffect(img)

cv.waitKey(0)
cv.destroyAllWindows()
