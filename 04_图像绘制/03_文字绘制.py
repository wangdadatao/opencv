"""
线段绘制
"""
import cv2 as cv
import numpy as np


def wordImg(image):
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.rectangle(image, (200, 200), (400, 400), (0, 255, 255), 3)

    cv.putText(image,  # 目标图片
               "haha",  # 文字内容
               (100, 300),  # 起始位置
               font,  # 字体类型
               2,  # 字体大小
               (100, 155, 255),  # 颜色
               2,  # 字体粗细
               cv.LINE_AA)

    cv.imshow("word_img", image)


img = cv.imread("../imgs/1.jpg", 1)
wordImg(img)

cv.waitKey(0)
cv.destroyAllWindows()
