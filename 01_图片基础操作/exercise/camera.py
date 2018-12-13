

import numpy as np
import cv2
import os

# VideoCapture既支持视频文件的读取也支持从摄像机中读取视频
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    os._exit(-1)

# 对象创建成功后isOpened()将返回true
while True:
    # 一帧一帧的捕获
    ret, frame = cap.read()
    if not ret:
        break

    # h, w, ch = frame.shape
    # blank = np.ones([h, w, ch], frame.dtype)
    #
    # dst = cv2.addWeighted(frame, 0.5, blank, 0.5, 10)
    # cv2.imshow("contrast_brightness_demo", dst)

    cv2.imshow('frame', frame)

    # waitKey(int delay)这个函数接收一个整形值,
    # 如果这个值是零,那么函数不会有返回值,如果delay大于0
    # 那么超过delayms后,如果没有按键,那么会返回-1,如果按键
    # 会返回键盘值,在某些系统中,返回的键盘值可能不是ASCII编码
    # 的,所以通过与0xFF进行与运算只取最后一个字节
    if (cv2.waitKey(10) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
