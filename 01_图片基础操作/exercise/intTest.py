import cv2 as cv
import numpy as np


def cv_resize(image, i):
    h, w, ch = image.shape
    dst = image[0: h, 82:462]

    dstHeight = 128
    dstWidth = 64
    dst = cv.resize(dst, (dstWidth, dstHeight))

    fileName = "D:/Documents/python/cup/poss/" + str(i) + ".jpg"
    cv.imwrite(fileName, dst, [cv.IMWRITE_JPEG_QUALITY, 100])


i = 510
for m in range(0, 2935):
    img = cv.imread("D:/Documents/python/cup/pos/image" + str(i) + ".jpg")
    cv_resize(img, i)
    i = i + 1

cv.waitKey(0)
cv.destroyAllWindows()
