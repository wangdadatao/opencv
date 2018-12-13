import cv2 as cv
import numpy as np


# 灰度直方图均衡化
def grayHistEqualize(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray_img", gray)

    # 直方图均衡化
    dst = cv.equalizeHist(gray)
    cv.imshow("grayHistEqualize", dst)


# 彩色直方图均衡化
def rgbHistEqualize(image):
    (b, g, r) = cv.split(image)  # 通道分解
    bH = cv.equalizeHist(b)
    gH = cv.equalizeHist(g)
    rH = cv.equalizeHist(r)

    dst = cv.merge((bH, gH, rH))  # 通道合成
    cv.imshow("rgbHistEqualize", dst)


# YUV 图片均衡化
def yuvHisEqualize(image):
    imgYUV = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)

    channelYUV = cv.split(imgYUV)
    channelYUV[0] = cv.equalizeHist(channelYUV[0])

    dst = cv.merge((channelYUV[0], channelYUV[1], channelYUV[2]))  # 通道合成
    dst = cv.cvtColor(dst, cv.COLOR_YCrCb2BGR)
    cv.imshow("yuvHisEqualize", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

grayHistEqualize(img)
rgbHistEqualize(img)
yuvHisEqualize(img)

cv.waitKey(0)
cv.destroyAllWindows()
