import cv2 as cv
import numpy as np


def mosaicImg(image):
    (h, w, ch) = image.shape
    for i in range(100, 500):
        for j in range(100, 500):
            if i % 50 == 0 and j % 50 == 0:
                for m in range(0, 50):
                    for n in range(0, 50):
                        (b, g, r) = image[i, j]
                        image[m + i, n + j] = (b, g, r)
    cv.imshow("mosaic_img", img)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

mosaicImg(img)

cv.waitKey(0)
cv.destroyAllWindows()
