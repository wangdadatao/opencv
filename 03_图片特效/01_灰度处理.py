import cv2 as cv
import numpy as np

"""
灰度图像：很多图像操作的基础（人脸识别， 边缘检测，行人识别。。。）
实时性：

"""


# 调用CV 自带接口
def cvtColorGray(image):
    grayImg = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 参数1：原始待转换图片的数据； 参数2：颜色转换的方式
    cv.imshow("grayImg", grayImg)
    print(grayImg.shape)  # 重新变为只有高 宽的二维图片


# RGB 均值法
# 灰度图像的 R=G=B  -> gray
def aveGrayImg(image):
    (h, w, ch) = image.shape
    dst = np.zeros((h, w, 3), np.uint8)

    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            gray = (int(b) + int(g) + int(r)) / 3
            dst[i, j] = np.uint8(gray)

    cv.imshow("aveGrayImg", dst)


# RGB 系数法
def coeGrayImg(image):
    (h, w, ch) = image.shape
    dst = np.zeros((h, w, 3), np.uint8)

    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            b = int(b)
            g = int(g)
            r = int(r)
            gray = r * 0.1 + g * 0.2 + b * 0.7
            dst[i, j] = np.uint8(gray)

    cv.imshow("coeGrayImg", dst)


# img1 = cv.imread("../imgs/1.jpg", 0)


# cv.imshow("img1", img1)
# print(img1.shape)  # 只有宽高两个维度

img2 = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img2", img2)
print(img2.shape)

# cvtColorGray(img2)
# aveGrayImg(img2)
coeGrayImg(img2)

cv.waitKey(0)

cv.destroyAllWindows()
