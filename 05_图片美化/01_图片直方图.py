import cv2 as cv
import numpy as np


def imageHist(image, type):
    color = (255, 255, 255)
    windowName = "Gray"
    if type == 0:
        color = (255, 0, 0)
        windowName = "B Hist"
    elif type == 1:
        color = (0, 255, 0)
        windowName = "G Hist"
    elif type == 2:
        color = (0, 0, 255)
        windowName = "R Hist"

    # 计算图片的直方图
    hist = cv.calcHist([image],  # 图片数据
                       [0],  # 计算直方图的通道
                       None,  # mask 蒙版
                       [256],  # 直方图的size， （有多少个柱状）
                       [0.0, 255.0]  # 直方图中各个像素的值
                       )

    minV, maxV, minL, maxL = cv.minMaxLoc(hist)

    histImg = np.zeros([256, 256, 3], np.uint8)

    for h in range(256):
        intenNormal = int(hist[h] * 256 / maxV)
        cv.line(histImg, (h, 256), (h, 256 - intenNormal), color)

    cv.imshow(windowName, histImg)


img = cv.imread("../imgs/1.jpg", 1)
cv.imshow("img", img)

channels = cv.split(img)  # 分解成三个颜色的通道 B G R
for i in range(3):
    imageHist(channels[i], i)

cv.waitKey(0)
cv.destroyAllWindows()
