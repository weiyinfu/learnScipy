import math

import numpy as np
import pylab as pl
from scipy.optimize import leastsq


def f(x, p):
    A, w, phi = p
    return A * np.sin(w * x + phi)


def residual(p, y, x):
    return y - f(x, p)


x = np.linspace(0, 2 * math.pi, 40, True)
y0 = f(x, (12, 1, 0))
y1 = y0 + np.random.randn(len(y0))
p0 = [10, 2, 3]
ans = leastsq(residual, p0, args=(y1, x))
print(ans)

pl.plot(x, y0, label="real data")
pl.plot(x, y1, label="noisy data")
pl.plot(x, f(x, ans[0]), label="mine data")
pl.legend()
pl.show()
