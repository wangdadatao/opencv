"""
使用已经训练好的模型人脸识别

"""

import cv2 as cv
import numpy as np

# 引入xml文件
face_xml = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread("../imgs/lena.jpg", 1)
cv.imshow("img", img)

# 转成灰度图片
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# detect 检测 p1: 灰度图片的数据  p2：缩放系数    p3：目标大小 （像素）
faces = face_xml.detectMultiScale(gray, 1.3, 5)
print("face = ", len(faces))

# 绘制人脸
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_face = gray[y:y + h, x: x + w]
    roi_color = img[y: y + h, x: x + w]

    eyes = eye_xml.detectMultiScale(roi_face)
    print("eye=", len(eyes))

    for (eX, eY, eW, eH) in eyes:
        cv.rectangle(roi_color, (eX, eY), (eX + eW, eY + eH), (0, 255, 0), 2)
cv.imshow("dst", img)

cv.waitKey(0)
