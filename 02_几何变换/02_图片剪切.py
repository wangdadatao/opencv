import cv2 as cv
import numpy as np


def img_cut(image):
    dst = image[100: 400, 100:400]
    cv.imshow("dst_img", dst)

    cv.waitKey(0)


img = cv.imread("../imgs/1.jpg")
cv.imshow("img", img)

img_cut(img)

cv.waitKey(0)
cv.destroyAllWindows()
