import random

import numpy as np
import cv2 as cv


# 图片反色
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    print("width: %s ;height: %s ;channls: %s" % (width, height, channels))

    for i in range(height):
        for j in range(width):
            for c in range(channels):
                pv = image[i, j, c]
                image[i, j, c] = 255 - pv

    cv.imshow("new img", image)


def create_img():
    # 单通道图片
    img = np.ones([1500, 1500, 3], np.uint8)
    for i in range(1500):
        for j in range(1500):
            img[i, j, 0] = random.randint(1, 255)
            img[i, j, 1] = random.randint(1, 255)
            img[i, j, 2] = random.randint(1, 255)

    cv.imshow("new img", img)

    '''
    三通道图片
    newImg = np.zeros([400, 400, 3], np.uint8)
    newImg[:, :, 0] = np.ones([400, 400]) * 100
    cv.imshow("new Img", newImg)
    
    :return: 
    '''


img = cv.imread("car.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)

create_img()

'''
# 计算运行反色消耗时间
t1 = cv.getTickCount()
access_pixels(img)
t2 = cv.getTickCount()
print("time: %s " % ((t2 - t1) / cv.getTickFrequency() * 1000))
'''

cv.waitKey(0)
