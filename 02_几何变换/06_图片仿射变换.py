import cv2 as cv
import numpy as np


def cv_api(image):
    h, w, ch = image.shape

    matSrc = np.float32([[0, 0], [0, h - 1], [w - 1, 0]])  # 定位三个点
    matDst = np.float32([[0, h - 1], [w - 1, h - 1], [0, 0]])  # 要放射到的位置

    matAffine = cv.getAffineTransform(matSrc, matDst)  # 得到矩阵组合，参数1：原来图像的三个点（左上角， 左下角，右上角）。 参数2： 新的坐标点

    dst = cv.warpAffine(image, matAffine, (w, h))  # 参数1：原始图片 参数2：移位矩阵 参数3：图片信息
    # 移位 矩阵
    cv.imshow("dst_img", dst)
    cv.waitKey(0)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)
cv_api(img)

cv.waitKey(0)
cv.destroyAllWindows()
