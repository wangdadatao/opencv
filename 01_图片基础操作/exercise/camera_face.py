import numpy as np
import cv2 as cv
import os
import time

# 引入xml文件
face_xml = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# VideoCapture既支持视频文件的读取也支持从摄像机中读取视频
cap = cv.VideoCapture(0)
if not cap.isOpened():
    os._exit(-1)

# 对象创建成功后isOpened()将返回true
while True:
    # 一帧一帧的捕获
    ret, frame = cap.read()
    if not ret:
        break

    # 转成灰度图片
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_xml.detectMultiScale(gray, 1.3, 5)

    # 绘制人脸
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        fileName = "faceImg/image" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + ".jpg"
        print(fileName)
        cv.imwrite(fileName, frame, [cv.IMWRITE_JPEG_QUALITY, 100])

    cv.imshow("dst", frame)

    if (cv.waitKey(10) & 0xFF) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
