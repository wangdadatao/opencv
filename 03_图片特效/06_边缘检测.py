"""
本质：卷积运算
canny 边缘检测： 1：灰度处理； 2：高斯滤波（去掉噪声干扰） 3：调用canny方法

sobel 算法算法原子：
    算子模版
        水平方向
        竖直方向
    图片卷积
    阈值判决


"""
import random
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


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

cannyImg(img)

cv.waitKey(0)
cv.destroyAllWindows()
