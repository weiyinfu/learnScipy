import numpy as np
import scipy.optimize as opt


def test_fmin(fmin, x, h, y, yn, h0):
    def convolve(h):
        return np.sum((yn - np.convolve(x, h)) ** 2)

    ans = fmin(convolve, h0)  # 求convolve函数的最小值
    print("=" * 20)
    print(fmin.__name__)
    print('h relative error', np.sum((h - ans) ** 2) / np.sum(h ** 2))


def test(m, n, nscale):
    x = np.random.rand(m)
    h = np.random.rand(n)
    y = np.convolve(x, h)
    yn = y + np.random.rand(len(y)) * nscale
    h0 = np.random.rand(n)
    test_fmin(opt.fmin, x, h, y, yn, h0)
    test_fmin(opt.fmin_bfgs, x, h, y, yn, h0)
    test_fmin(opt.fmin_cg, x, h, y, yn, h0)
    test_fmin(opt.fmin_powell, x, h, y, yn, h0)


def f2(x):
    return x * x + 3 * x + 7


def simple_sample():
    x = opt.fmin(f2, 0)
    print(x, f2(x))


test(200, 20, 0.1)
simple_sample()
