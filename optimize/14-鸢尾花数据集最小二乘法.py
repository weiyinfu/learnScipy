import numpy as np
import sklearn.datasets as d

from scipy.optimize import leastsq

"""
有时候能够得到不错的结果：0.9866666
"""
x, y = d.load_iris(True)
print(x.shape, y.shape)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)


step = 0


def get_loss(p, y_true, x):
    global step
    step += 1
    w1, b, w2 = parse(p, pattern)
    y = sigmoid(np.matmul(x, w1) + b)
    y = np.matmul(y, w2)
    y = softmax(y)
    pred = np.argmax(y, axis=1)
    y = y[np.arange(len(y)), y_true]
    r = -np.log(y)
    if step % 1000 == 1:
        prec = np.count_nonzero(pred == y_true) / len(x)
        print(f'step={step} loss={np.mean(r)} prec={prec}')
    return r


w1 = np.random.random((4, 10))
b = np.random.random(10)
w2 = np.random.random((10, 3))
pattern = (w1, b, w2)


def pack(a) -> np.ndarray:
    return np.concatenate([i.reshape(-1) for i in a])


def parse(a, pattern):
    ans = []
    s = 0
    for i in pattern:
        nex = s + np.prod(i.shape)
        ans.append(a[s:nex].reshape(i.shape))
        s = nex
    return ans


"""
把ftol，xtol设置成0，则能够让他们不生效
ftol：相当于y的相对误差限
xtol:相当于x的相对误差限
maxfev：max function eval count,最多调用get_loss函数的次数
"""
ans = leastsq(get_loss, x0=pack((w1, b, w2)), args=(y, x), ftol=1e-30, xtol=1e-20, maxfev=2000000)
print(ans)
