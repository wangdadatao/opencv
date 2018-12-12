import cv2 as cv
import numpy as np


def get_img_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def video_demo():
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


img = cv.imread("car.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)
cv.imwrite("/2.jpg", img)

get_img_info(img)
# video_demo()
cv.waitKey(0)
