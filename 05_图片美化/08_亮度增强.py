"""
最简单的亮度增强/美白：
    目标亮度= 当前亮度 + 常量
"""

import cv2 as cv
import numpy as np


def brightness(image):
    (h, w, ch) = image.shape
    dst = np.zeros((h, w, 3), np.uint8)

    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            bb = 255 if int(b) + 40 >= 255 else int(b) + 40
            gg = 255 if int(g) + 40 >= 255 else int(g) + 40
            rr = 255 if int(r) + 40 >= 255 else int(r) + 40
            dst[i, j] = (bb, gg, rr)

    cv.imshow("dst_img", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

brightness(img)

cv.waitKey(0)
cv.destroyAllWindows()
