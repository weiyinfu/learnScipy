import scipy.io as sio
from PIL import Image

import numpy as np

x, y = np.random.randint(0, 100, (2, 10))
z = x + y
print(x)
sio.savemat('orl', {
    "x": x, "y": y, "z": z
})

a = sio.loadmat("orl.mat")
print(a)
x, y, z = a['x'], a['y'], a['z']
print(x)  # 注意：此处x为二维矩阵，使用mat保存的数组至少是二维，即便是1维也会转成2维
