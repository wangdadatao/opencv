"""
HOG 特征：
    步骤：
        1：模块划分
            image
            windows窗体：
                特征计算的最顶层单元：包含所有的目标信息
                窗体的大小是任意的
                step: 滑动步长
            block：
                block小于windows的大小
                windows的大小一般是block的整数倍
                step: 滑动步长
                    block 对windows遍历是滑动步长
            cell
                size:  参考上一层block
                不可滑动

            image > windows > block > cell (包含 大于)
        2：根据模版计算梯度、方向
            每个像素的梯度：
                大小（浮值），
                方向：
                    比如：360度 每40度划分一块，可以划分9块，那么可以理解为有9个bin
                        cell 包含完整360度的信息，包含9个bin
        3：bin的投影
        4：计算每个模块的hog特征
            hog 特征维度：
                hog特征得到的是向量：完整描述目标的所有信息
                维度 = block 个数 * 每个block中cell的个数 * 每个cell中bin的个数

"""

"""

梯度：
    像素都有一个梯度
    利用特征模版计算：
        水平方向:
            模版：[1, 0, -1]
            计算过程：左中右三个像素与模版相乘 a = p1 * 1 + p2 *0 + p3 * (-1) = p1 -p3 
            本质：相邻像素只差            
        竖直方向:
            模板：[[1],[0],[-1]]
            本质：上下像素之差 b
    梯度 f = 根号下（a方 + b方）
    方向 angle  = arctan(a/b)
    
"""
