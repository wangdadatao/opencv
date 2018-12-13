"""
本质：卷积运算
canny 边缘检测： 1：灰度处理； 2：高斯滤波（去掉噪声干扰） 3：调用canny方法

sobel 算法算法原子：
    算子模版
        水平方向 (模版):
            [[1,2,3],
             [0,0,0],
             [-1,-2,-1]]
        竖直方向 (模版):
            [[1,0,-1],
             [2,0,-2],
             [1,0,-1]]
    图片卷积
    阈值判决
"""
import math

import cv2 as cv
import numpy as np


def cannyImg(image):
    (h, w, ch) = image.shape

    # 灰度处理
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # 高斯滤波
    gaussian = cv.GaussianBlur(gray, (3, 3), 0)  # 参数1：灰度图像数据； 参数2：模版大小

    # 卷积运算
    dst = cv.Canny(gaussian, 100, 100)  # 参数1：图片数据，参数2，3：门限 图片经过卷积运算后大于门限值，则认为此点事边缘点
    cv.imshow("canny_img", dst)


# sobel算子： 1：算子模版   2：图片卷积  3：阈值判决
def sobel(image):
    (h, w, ch) = image.shape
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    dst = np.zeros((h, w, 1), np.uint8)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            gy = gray[i - 1, j - 1] * 1 + gray[i - 1, j] * 2 + gray[i - 1, j + 1] * 1 - gray[i + 1, j] * 1 - gray[
                i + 1, j] * 2 - gray[i + 1, j + 1] * 1
            gx = gray[i - 1, j - 1] + gray[i, j - 1] * 2 + gray[i + 1, j - 1] - gray[i - 1, j + 1] - gray[
                i, j + 1] * 2 - gray[i + 1, j + 1]

            grad = math.sqrt(gx * gx + gy * gy)
            if grad > 100:
                dst[i, j] = 255
            else:
                dst[i, j] = 0

    cv.imshow("dsobel_img", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

cannyImg(img)
sobel(img)

cv.waitKey(0)
cv.destroyAllWindows()
