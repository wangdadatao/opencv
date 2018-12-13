"""
线段绘制
"""
import cv2 as cv
import numpy as np


def shapeImg():
    dst = np.zeros((800, 800, 3), np.uint8)

    # 绘制矩形 p1: 目标图片；    p2：矩形左上角；   p3：矩形右下角；   p4：颜色；  p5：是否填充（-1：需要填充；大于0时：线条宽度）
    cv.rectangle(dst, (100, 100), (200, 200), (0, 255, 255), -1)

    # 绘制圆形 p1: 目标图片；    p2：圆心坐标；   p3：半径；   p4：颜色；  p5：是否填充（-1：需要填充；大于0时：线条宽度）
    cv.circle(dst, (400, 400), 100, (255, 255, 9), 2)

    # 绘制扇形
    cv.ellipse(dst,  # 目标图片
               (600, 500),  # 椭圆中心
               (150, 300),  # 椭圆长轴和短轴的长度
               30,  # 长轴倾角
               90,  # 弧度绘制的起始角度
               180,  # 弧度绘制的结束角度
               (255, 255, 9),  # 颜色
               10,  # 是否填充（-1：需要填充；大于0时：线条宽度）
               cv.LINE_AA,  # 线型
               0  # 偏移量
               )

    # 绘制多边形
    points = np.array([[50, 50], [200, 100], [600, 400], [300, 300], [50, 50]])

    # 矩阵转置
    # TODO 查询具体转置意义
    points = points.reshape((-1, 1, 2))
    cv.polylines(dst, [points], True, (100, 255, 100))

    cv.imshow("shape_img", dst)


shapeImg()

cv.waitKey(0)
cv.destroyAllWindows()
