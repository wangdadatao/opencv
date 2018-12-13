"""
油画效果：
    1: 灰度
    2：分割若干个小方块，统计里面的灰度值
    3：0-255 灰度值分为若干个等级， 把第2步的结果映射到等级里
    4：灰度段中灰度个数的统计
    5：第四步统计出来的平均值替代当前值
"""
import math
import cv2 as cv
import numpy as np


def oilPainting(image):
    (h, w, ch) = image.shape
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = np.zeros((h, w, 3), np.uint8)

    for i in range(4, h - 4):
        for j in range(4, w - 4):
            (b, g, r) = image[i, j]

            # 定义灰度等级
            # 求出每个灰度的个数
            array1 = np.zeros(8, np.uint8)
            for m in range(-4, 4):
                for n in range(-4, 4):
                    p1 = int(gray[i + m, j + n] / 32)
                    array1[p1] = array1[p1] + 1

            # 找到像素所在灰度等级最多的那个灰度段l
            currentMax = array1[0]
            l = 0
            for k in range(0, 8):
                if currentMax < array1[k]:
                    currentMax = array1[k]
                    l = k

            # 找到在灰度段l中的颜色值
            for m in range(-4, 4):
                for n in range(-4, 4):
                    if (l * 32) <= gray[i + m, j + n] <= ((l + 1) * 32):
                        (b, g, r) = image[i + m, j + m]
                        break

            dst[i, j] = (b, g, r)

    cv.imshow("oil_painting", dst)


img = cv.imread("../imgs/messi5.jpg", 1)
cv.imshow("img", img)

oilPainting(img)

cv.waitKey(0)
cv.destroyAllWindows()
