"""
1 思想：分类器
2 寻找一个最优超平面
3 核 本例应用线性核
4 样本：数量可以不相同
    正样本
    负样本
5 训练：
    SVM: SVM_create（创建）-> train(训练） -> predict(预测）

SVM 支持向量机（分类器）
    本质：寻求一个最优的超平面 分类

例子：身高-体重分类 预测
"""
import cv2 as cv
import numpy as np
import matplotlib as plt

# 数据准备 男女生身高数据
rand1 = np.array([[155, 48], [159, 50], [165, 53], [170, 56], [163, 51]])
rand2 = np.array([[153, 55], [163, 57], [171, 61], [180, 70], [176, 62]])

# 准备标签
# 所有的数据都要有标签：描述当前数据的真实属性情况
# 有标签的数据：监督学习 0：负样本 1：正样本
label = np.array([[0], [0], [0], [0], [0], [1], [1], [1], [1], [1]])

# 处理数据
data = np.vstack((rand1, rand2))  # 合并数据
data = np.array(data, dtype='float32')

# SVM训练
svm = cv.ml.SVM_create()  # ml:机器学习模块 创建

# 属性设备
svm.setType(cv.ml.SVM_C_SVC)  # 设备SVM类型
svm.setKernel(cv.ml.SVM_LINEAR)  # 设置内核， 本例选用线性内核
svm.setC(0.01)

# 训练
result = svm.train(data, cv.ml.ROW_SAMPLE, label)

# 预测
ptDate = np.vstack([[167, 55], [162, 80]])
ptDate = np.array(ptDate, dtype='float32')

# print(ptDate)
(par1, par2) = svm.predict(ptDate)
print(par2)
