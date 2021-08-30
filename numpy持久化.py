"""
numpy保存数组有两种方式：二进制方式和文本方式
二进制方式保存数组只能保存成不知道什么类型的一维数组
文本方式保存只能保存一维数组和二维数组，不能保存高维数组
"""

import numpy as np
a=[1,2,3]
b=[[1,2],[3,4]]
np.savetxt("a.txt",a)
np.savetxt("b.txt",b)
aa=np.loadtxt("a.txt")
bb=np.loadtxt("b.txt")
print(aa)
print(bb)