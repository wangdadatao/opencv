"""
磨皮美白：
    双边滤波：


"""

import cv2 as cv
import numpy as np

img = cv.imread("../imgs/stripe_girl.jpg", 1)
cv.imshow("img", img)

dst = cv.bilateralFilter(img, 15, 35, 35)
cv.imshow("dst_img", dst)

cv.waitKey(0)
cv.destroyAllWindows()
