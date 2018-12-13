"""
图片修补：
    1：生成坏了的图片
    2：扎到"坏"的位置
    3：调用api完成修补
"""

import cv2 as cv
import numpy as np


def repairImg(image):
    (h, w, ch) = image.shape

    # 定义蒙版
    paint = np.zeros((h, w, 1), np.uint8)

    # 因为明确的知道坐标所以可以精确处理
    for i in range(200, 300):
        paint[i, 200] = 255
        paint[i, 200 + 1] = 255
        paint[i, 200 - 1] = 255

    for i in range(150, 250):
        paint[250, i] = 255
        paint[250 + 1, i] = 255
        paint[250 - 1, i] = 255
    cv.imshow("蒙版", paint)

    imgDst = cv.inpaint(image, paint, 3, cv.INPAINT_TELEA)
    cv.imshow("dst_img", imgDst)


img = cv.imread("../imgs/apple.jpg", 1)
cv.imshow("img", img)

# 破坏图片
for i in range(200, 300):
    img[i, 200] = (255, 255, 255)
    img[i, 200 + 1] = (255, 255, 255)
    img[i, 200 - 1] = (255, 255, 255)

for i in range(150, 250):
    img[250, i] = (255, 255, 255)
    img[250 + 1, i] = (255, 255, 255)
    img[250 - 1, i] = (255, 255, 255)

cv.imshow("img", img)
repairImg(img)

cv.waitKey(0)
cv.destroyAllWindows()
