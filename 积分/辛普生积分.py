import numpy as np
from scipy import integrate

"""
新普生积分是一种采样积分
"""
x = np.linspace(0, 1, 129)
y = np.sin(x)
simpson = integrate.simps(y, x)
print(simpson)
print(np.cos(0) - np.cos(1))

# 注意：len(y)必须等于1+2的整数幂，否则romb积分无法使用，romb积分精度非常高
romb = integrate.romb(y, dx=x[1] - x[0])
print(romb)
