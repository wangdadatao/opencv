import cv2 as cv

img = cv.imread("../imgs/1.jpg", 1)
(h, w, ch) = img.shape
size = (w, h)
print(size)

# 写入对象创建 p1: 名称；p2：编码器  p3：帧率   p4：大小
videoWrite = cv.VideoWriter("writeVideos/1.mp4", -1, 5, size)

for i in range(1, 100):
    fileName = "image" + str(i) + ".jpg"
    img = cv.imread(fileName)
    videoWrite.write(img)
