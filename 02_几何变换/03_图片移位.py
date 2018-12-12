import cv2 as cv
import numpy as np


def cv_api(image):
    h, w, ch = image.shape
    matShitf = np.float32([[1, 0, 50], [0.99, 2, -100]])  # 两行三列
    dst = cv.warpAffine(image, matShitf, (w, h))  # 参数1：原始图片 参数2：移位矩阵 参数3：图片信息
    # 移位 矩阵
    cv.imshow("dst_img", dst)
    cv.waitKey(0)


def shifting_img(image, dH, dW):
    dst = np.zeros(image.shape, np.uint8)

    h, w, ch = image.shape
    for i in range(0, h - dH):
        for j in range(0, w - dW):
            dst[i + dH, j + dW] = image[i, j]

    cv.imshow("shift_dst_img", dst)
    cv.waitKey(0)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)
shifting_img(img, 100, 100)

cv.waitKey(0)
cv.destroyAllWindows()
