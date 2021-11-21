import numpy as np
from scipy import integrate

func = lambda x0, x1, x2, x3: x0 ** 2 + x1 * x2 - x3 ** 3 + np.sin(x0) + (
    1 if (x0 - .2 * x3 - .5 - .25 * x1 > 0) else 0)


def opts0(*args, **kwargs):
    return {'points': [0.2 * args[2] + 0.5 + 0.25 * args[0]]}


integrate.nquad(func, [[0, 1], [-1, 1], [.13, .8], [-.15, 1]],
                opts=[opts0, {}, {}, {}], full_output=True)
