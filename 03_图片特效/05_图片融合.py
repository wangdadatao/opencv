import random

import cv2 as cv
import numpy as np


# 图片融合
# 两张图片必须像素相同
def fuseImg(image1, image2):
    (h1, w1, ch1) = image1.shape
    (h2, w2, ch2) = image2.shape

    roiH = int(h1 / 2)
    roiW = int(w1 / 2)
    img1Roi = image1[0:roiH, 0:roiW]
    img2Roi = image2[0:roiH, 0:roiW]

    # dst = np.zeros([roiH, roiW, 3], np.uint8)
    dst = cv.addWeighted(img1Roi, 0.5, img2Roi, 0.5, 0)
    cv.imshow("fuseImg", dst)


# 毛别离效果 image:图片信息， num：毛玻璃像素
def frostedGlassImg(image, num):
    (h, w, ch) = image.shape
    dst = np.zeros([h, w, 3], np.uint8)

    for i in range(0, h):
        for j in range(0, w):
            index = int(random.random() * num)
            nH = i - index if i + index >= h else i + index
            nW = j - index if j + index >= w else j + index
            (b, g, r) = image[nH, nW]
            dst[i, j] = (b, g, r)

    return dst


def testFuseImg(image):
    image2 = frostedGlassImg(image, 100)
    dst = cv.addWeighted(image, 0.5, image2, 0.5, 0)
    cv.imshow("testFuseImg", dst)


img1 = cv.imread("../imgs/1.jpg", 1)
img2 = cv.imread("../imgs/aero1.jpg", 1)
cv.imshow("img1", img1)
cv.imshow("img2", img2)

testFuseImg(img1)

cv.waitKey(0)
cv.destroyAllWindows()
