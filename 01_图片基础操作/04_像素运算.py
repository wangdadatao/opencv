import cv2 as cv
import numpy as np


# 两张图片相加
def add_demo(image1, image2):
    dst = cv.add(image1, image2)
    cv.imshow("add_demo", dst)


# 两张图片相减
def subtract_demo(image1, image2):
    dst = cv.subtract(image1, image2)
    cv.imshow("subtract_demo", dst)


# 两张图片相除
def divide_demo(image1, image2):
    dst = cv.divide(image1, image2)
    cv.imshow("divide_demo", dst)


# 两张图片相乘
def multiply_demo(image1, image2):
    dst = cv.multiply(image1, image2)
    cv.imshow("multiply_demo", dst)


# 逻辑运算
def logic_demo(image1, image2):
    andImg = cv.bitwise_and(image1, image2)
    cv.imshow("andImg", andImg)

    notImg = cv.bitwise_not(image1)
    cv.imshow("notImg", notImg)

    orImg = cv.bitwise_or(image1, image2)
    cv.imshow("orImg", orImg)

    xorImg = cv.bitwise_xor(image1, image2)
    cv.imshow("orImg", xorImg)


def others(image1, image2):
    m1 = cv.mean(image1)  # 求均值
    m2 = cv.mean(image2)

    m3, dev3 = cv.meanStdDev(image1)  # 结果1：均值； 结果2：方差

    print(m1)
    print(m2)


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([w, h, ch], image.dtype)

    # 图片融合
    dst = cv.addWeighted(image, c, blank, 1 - c, b)
    cv.imshow("contrast_brightness_demo", dst)


img1 = cv.imread("../imgs/LinuxLogo.jpg")
img2 = cv.imread("../imgs/WindowsLogo.jpg")
print(img1.shape)  # 获取高 款 通道数
print(img2.shape)

cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img1)
cv.imshow("img2", img2)

# add_demo(img1, img2)
# subtract_demo(img1, img2)
# divide_demo(img1, img2)
# multiply_demo(img1, img2)

# others(img1, img2)

logic_demo(img1, img2)

cv.waitKey(0)
cv.destroyAllWindows()
