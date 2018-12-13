"""
中值滤波
"""

import cv2 as cv
import numpy as np


def medianFiltering(image):
    (h, w, ch) = image.shape
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray_img", gray)

    dst = np.zeros((h, w, 3), np.uint8)
    collect = np.zeros(25, np.uint8)

    for i in range(3, h - 3):
        for j in range(3, w - 3):
            k = 0
            for m in range(-2, 3):
                for n in range(-2, 3):
                    collect[k] = gray[i + m, j + n]
                    k += 1

            collect = np.sort(collect, axis=0, kind="quicksort", order=None)
            dst[i, j] = collect[13]

    cv.imshow("dst_img", dst)


img = cv.imread("../imgs/ela_modified.jpg", 1)
cv.imshow("img", img)
medianFiltering(img)

cv.waitKey(0)
cv.destroyAllWindows()
