import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

"""
折线图积分，求积分函数
"""
x = np.linspace(-np.pi, np.pi, 100)
ans = integrate.cumtrapz(np.sin(x), x, initial=0)

plt.plot(x, ans, x, np.sin(x))
plt.show()
