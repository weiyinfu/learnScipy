import numpy as np
import 学习scipy.interpolate as interpolate
import pylab as pl

x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
pl.plot(x, y, 'o', label='the original data')

x_new = np.linspace(0, 2 * np.pi, 100)
y_linear = interpolate.interp1d(x, y)
pl.plot(x_new, y_linear(x_new), label="linear interpolate")
tck = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, tck)
pl.plot(x_new, y_bspline, label="B spline")
pl.legend()
pl.show()
