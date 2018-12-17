"""
视频分解图片：
    1：加载视频
    2：读取info信息
    3：parse 解码 获取单帧信息
    4：处理
"""
import cv2 as cv

cap = cv.VideoCapture(0)
isOpened = cap.isOpened()
print(isOpened)

# 帧率 ：每秒展示的图片
fps = cap.get(cv.CAP_PROP_FPS)
print(fps)

# 宽度
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))

# 高度
heigh = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

i = 0
while (isOpened):
    if i == 100:
        break
    else:
        i = i + 1

    # 读取每一帧， flat:是否读取成功 frame: 当前帧信息
    (flag, frame) = cap.read()

    fileName = "writeVideos/image" + str(i) + ".jpg"
    print(fileName)

    if flag:
        cv.imwrite(fileName, frame, [cv.IMWRITE_JPEG_QUALITY, 100])
