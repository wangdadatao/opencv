import cv2 as cv
import numpy as np


def zoom_img(image):
    h, w, ch = image.shape

    matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
    dstImg = cv.warpAffine(image, matScale, (int(w / 2), int(h / 2)))

    cv.imshow("dstImg", dstImg)
    cv.waitKey(0)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

zoom_img(img)

cv.waitKey(0)
cv.destroyAllWindows()
