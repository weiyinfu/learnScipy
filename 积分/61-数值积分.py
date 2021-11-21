import numpy as np

x = np.linspace(0, 1, 100)
y = np.sqrt(1 - x ** 2)
# 简单方法计算面积
s = np.sum(y[:-1] * 1 / len(x))
print(s * 4)
# trapz计算面积
s = np.trapz(y, x)  # 折线段的面积
print(s * 4)

import scipy.integrate as integrate

# 调用库函数积分
s, err = integrate.quad(lambda x: np.sqrt(1 - x * x), 0, 1)
print(s * 4, err)

# 计算二重积分
s, err = integrate.dblquad(lambda x, y: np.sqrt(1 - x * x - y * y), 0, 1, lambda x: 0, lambda x: np.sqrt(1 - x * x))
print(s * 8 / (4 / 3), err)
