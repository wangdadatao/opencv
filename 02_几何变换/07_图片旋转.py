import cv2 as cv
import numpy as np


def cv_api(image):
    h, w, ch = image.shape

    maRotate = cv.getRotationMatrix2D((w * 0.5, h * 0.5), 90, 1)  # 参数1： 图片的中心点  参数2：旋转角度； 参数3：缩放的系数

    dst = cv.warpAffine(image, maRotate, (w, h))

    # 移位 矩阵
    cv.imshow("dst_img", dst)
    cv.waitKey(0)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)
cv_api(img)

cv.waitKey(0)
cv.destroyAllWindows()
