import cv2 as cv

cap = cv.VideoCapture("D:/Documents/python/cup/6.mp4")
isOpened = cap.isOpened()
print(isOpened)

# 帧率 ：每秒展示的图片
fps = cap.get(cv.CAP_PROP_FPS)
print(fps)

# 宽度
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))

# 高度
heigh = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

i = 510
while (isOpened):

    # 读取每一帧， flat:是否读取成功 frame: 当前帧信息
    (flag, frame) = cap.read()

    if flag:
        fileName = "D:/Documents/python/cup/pos/image" + str(i) + ".jpg"
        cv.imwrite(fileName, frame, [cv.IMWRITE_JPEG_QUALITY, 100])

        i = i + 1
    else:
        break


