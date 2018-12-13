import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def imageHistEqualize(image):
    (h, w, ch) = image.shape
    countB = np.zeros(256, np.float)
    countG = np.zeros(256, np.float)
    countR = np.zeros(256, np.float)

    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            indexB = int(b)
            indexG = int(g)
            indexR = int(r)
            countB[indexB] = countB[indexB] + 1
            countG[indexG] = countG[indexG] + 1
            countR[indexR] = countR[indexR] + 1

    # 计算概率
    allPixel = h * w
    for i in range(0, 256):
        countB[i] = countB[i] / allPixel
        countG[i] = countG[i] / allPixel
        countR[i] = countR[i] / allPixel

    # 计算累积概率
    sumB = float(0)
    sumG = float(0)
    sumR = float(0)
    for i in range(0, 256):
        sumB = sumB + countB[i]
        countB[i] = sumB

        sumG = sumG + countG[i]
        countG[i] = sumG

        sumR = sumR + countR[i]
        countR[i] = sumR

    # 计算映射表
    mapB = np.zeros(256, np.uint16)
    mapG = np.zeros(256, np.uint16)
    mapR = np.zeros(256, np.uint16)
    for i in range(0, 256):
        mapB[i] = np.uint16(countB[i] * 255)
        mapG[i] = np.uint16(countG[i] * 255)
        mapR[i] = np.uint16(countR[i] * 255)

    # 映射
    for i in range(0, h):
        for j in range(0, w):
            (b, g, r) = image[i, j]
            image[i, j] = (mapB[b], mapG[g], mapR[r])

    cv.imshow("dst_img", image)


img = cv.imread("../imgs/apple.jpg", 1)
cv.imshow("img", img)

imageHistEqualize(img)

cv.waitKey(0)
cv.destroyAllWindows()
