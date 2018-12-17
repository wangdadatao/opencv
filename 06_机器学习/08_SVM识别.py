"""
1: 样本
    正样本
        包含所检测目标
        尽可能的多样（环境、干扰多样）
    负样本
        木能包含所检测的目标
    获取样本方法：
        1：网络
        2：公司内部
        3：自己收集
    一个好的样本远胜过一个复杂的神经网络
    数量：
        正：负数  最好 1:2 ~ 1:3
2：训练
3：预测

"""

import numpy as np
import cv2 as cv
import matplotlib as plt

# 1:定义参数
# 正负样本数量，与实际相同
PosNum = 820
NegNum = 1931

# 窗体大小
winSize = (64, 128)

blockSize = (16, 16)
blockStride = (8, 8)

cellSize = (8, 8)

nBin = 9

# 2：创建HOG对象 p1: windows p2:block大小  p3:block步长  p4:cell大小   p5:bin个数
hog = cv.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nBin)

# 3：SVM创建
svm = cv.ml.SVM_create()

# 4：计算HOG
featureNum = int(((128 - 16) / 8 + 1) * ((64 - 16) / 8 + 1) * 4 * 9)  # 3780

# 存放特征 二维
featureArray = np.zeros(((PosNum + NegNum), featureNum), np.float32)

# 标签 存放样本标签 监督学习
labelArray = np.zeros(((PosNum + NegNum), 1), np.int32)

# 处理正样本
for i in range(0, PosNum):
    fileName = "pos/" + str(i + 1) + ".jpg"
    img = cv.imread(fileName)
    # 计算Hog特征
    hist = hog.compute(img, (8, 8))  # 3780维
    for j in range(0, featureNum):
        featureArray[i, j] = hist[j]

    labelArray[i, 0] = 1

# 处理负样本
for i in range(0, NegNum):
    fileName = "neg/" + str(i + 1) + ".jpg"
    img = cv.imread(fileName)
    # 计算Hog特征
    hist = hog.compute(img, (8, 8))  # 3780维
    for j in range(0, featureNum):
        featureArray[i + PosNum, j] = hist[j]

    labelArray[i + PosNum, 0] = -1

# 5 设置SVM属性
svm.setType(cv.ml.SVM_C_SVC)
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setC(0.01)

# 6 训练
ret = svm.train(featureArray, cv.ml.ROW_SAMPLE, labelArray)

# 7 检测
alpha = np.zeros((1), np.float32)

# SVM 得到的HOG描述信息 （判决）
rho = svm.getDecisionFunction(0, alpha)

alphaArray = np.zeros((1, 1), np.float32)
supportVArray = np.zeros((1, featureNum), np.float32)
resultArray = np.zeros((1, featureNum), np.float32)
alphaArray[0, 0] = alpha
resultArray = -1 * alphaArray * supportVArray

myDetect = np.zeros((3781), np.float32)
for i in range(0, 3780):
    myDetect[i] = resultArray[0, i]

myDetect[3780] = rho[0]

# 构建HOG
myHog = cv.HOGDescriptor()
myHog.setSVMDetector(myDetect)

imageSrc = cv.imread('../imgs/aero1.jpg', 1)

# 用训练好的特征 对目标进行检测：
objs = myHog.detectMultiScale(imageSrc, 0, (8, 8), (32, 32), 1.01, 5)
x = int(objs[0][0][0])
y = int(objs[0][0][1])
w = int(objs[0][0][2])
h = int(objs[0][0][3])

# 目标绘制
cv.rectangle(imageSrc, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv.imshow("dst", imageSrc)
cv.waitKeyEx(0)
