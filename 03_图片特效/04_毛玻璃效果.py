import random

import cv2 as cv
import numpy as np


# 毛玻璃效果
# 缺点：像素往后取，有种拖影的感觉。 可优化为周围范围内随机取。
def frostedGlassImg(image):
    (h, w, ch) = image.shape
    dst = np.zeros([h, w, 3], np.uint8)
    mm = 5

    for i in range(0, h):
        for j in range(0, w):
            index = int(random.random() * mm)
            nH = i - index if i + index >= h else i + index
            nW = j - index if j + index >= w else j + index
            (b, g, r) = image[nH, nW]
            dst[i, j] = (b, g, r)

    cv.imshow("frosted_glass_img", dst)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

frostedGlassImg(img)

cv.waitKey(0)
cv.destroyAllWindows()
