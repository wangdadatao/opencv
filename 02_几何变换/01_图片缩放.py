import cv2 as cv
import numpy as np

"""
最近邻域插值法：
    src 10*20 dst 5*10
    dst <- src
    (1, 2) <- (2, 4)
    dst x -> src x 2 newX
    newX = x * (src 行/目标 行)  newX = 1 * (10/5) = 2
    newY = y * (src 列/目标 列)  newY = 2 * (20/10) = 4
    结果为小数时取整

双线性插值法：
    
"""


# 最近邻域插值法
def dst_demo(image):
    h, w, ch = image.shape
    dH = int(h / 2)
    dW = int(w / 2)

    print(h, w, dH, dW)

    dstImg = np.zeros([dH, dW, 3], np.uint8)

    for i in range(0, dH):
        for j in range(0, dW):
            iNew = int(i * (h / dH))
            jNew = int(j * (w / dW))
            dstImg[i, j] = image[iNew, jNew]

    cv.imshow("dstImg2", dstImg)
    cv.waitKey(0)
    return


# opencv 自带API
def cv_resize(image):
    h, w, ch = img.shape

    # 1: 放大，缩小 2：等比例 非
    dstHeight = int(h * 0.5)
    dstWidth = int(w * 0.5)

    # 最近邻域差值 双线性差值 像素关系重采样 立方差值
    dst = cv.resize(img, (dstWidth, dstHeight))
    cv.imshow("dst_img", dst)
    cv.imshow("img", img)


img = cv.imread("../imgs/1.jpg")
dst_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()
