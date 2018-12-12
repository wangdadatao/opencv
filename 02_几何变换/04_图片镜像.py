import cv2 as cv
import numpy as np


# 垂直镜像
def mirror_img(image):
    h, w, ch = image.shape
    print(h, w, ch)

    mirrorImg = np.zeros((h * 2, w, ch), np.uint8)
    for i in range(0, h):
        for j in range(0, w):
            mirrorImg[i, j] = image[i, j]
            # 方法1： 从镜像的最低端开始赋值
            # mirrorImg[h * 2 - i - 1, j] = image[i, j]

            # 方法2：从镜像的最上面开始赋值
            mirrorImg[h + i, j] = image[h - i - 1, j]

    cv.imshow("mirrorImg", mirrorImg)
    cv.waitKey(0)


img = cv.imread("../imgs/1.jpg", 1)
# cv.imshow("img", img)
mirror_img(img)
cv.waitKey(0)
cv.destroyAllWindows()
