import math

import numpy as np
import scipy.optimize as opt


def f(x):
    x0, x1, x2 = x[0], x[1], x[2]
    return [
        5 * x1 + 3,
        4 * x0 * x0 - 2 * math.sin(x1 * x2),
        x1 * x2 - 1.5
    ]


ans = opt.fsolve(f, np.array([1, 1, 1]))
print(ans, f(ans))


def jacobi(x):
    x0, x1, x2 = x[0], x[1], x[2]
    return [
        [5, 0, 0],
        [8 * x0, -2 * x2 * math.cos(x1 * x2), -2 * x1 * math.cos(x1 * x2)],
        [0, x2, x1]
    ]


ans = opt.fsolve(f, np.array([1, 1, 1]), fprime=jacobi)
print(ans, f(ans))
