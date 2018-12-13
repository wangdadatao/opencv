"""
线段绘制
"""
import cv2 as cv
import numpy as np


def lineImg():
    dst = np.zeros((800, 800, 3), np.uint8)

    # 绘制线段 p1: 目标图片数据； p2：线段初始位置；   p3：线段结束位置；  p4：颜色
    cv.line(dst, (100, 100), (200, 200), (0, 0, 255))

    # p5: 线条宽度
    cv.line(dst, (200, 200), (200, 100), (0, 0, 255), 20)

    # p6: 线条类型 LINE_4; LINE_8(默认值); LINE_AA(线段头部更加光滑——采用了高斯滤波)
    cv.line(dst, (200, 100), (400, 100), (0, 255, 0), 50, cv.LINE_AA)

    # 绘制三角形
    cv.line(dst, (400, 400), (200, 600), (255, 255, 0), 50, cv.LINE_AA)
    cv.line(dst, (200, 600), (600, 600), (255, 255, 0), 50, cv.LINE_AA)
    cv.line(dst, (600, 600), (400, 400), (255, 255, 0), 50, cv.LINE_AA)

    cv.imshow("lineImg", dst)


img = cv.imread("../imgs/1.jpg", 1)
# cv.imshow("img", img)

lineImg()

cv.waitKey(0)
cv.destroyAllWindows()
