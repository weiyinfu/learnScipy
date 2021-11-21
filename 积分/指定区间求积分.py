import numpy as np
from scipy import integrate as it


def f(x):
    return np.sin(x)


ans = it.quad(f, 0, 1)
print(ans)
print(np.cos(0) - np.cos(1))
"""
使用n阶高斯积分求积分，n默认为5
"""
print(it.fixed_quad(f, 0, 1, n=10))

print(it.quadrature(f, 0, 1))
