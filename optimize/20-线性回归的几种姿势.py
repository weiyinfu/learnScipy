import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

n = 100
x = np.linspace(0, 3, n)
y = 0.2 * x + 0.4 + np.random.random(n) * 0.3
"""
k,b：拟合的直线
r：相关系数
p：概率
sigma：方差
"""


def use_scipy():
    k, b, r, p, sigma = st.linregress(x, y)
    print(np.mean((y - k * x - b) ** 2), sigma)
    plt.plot(x, k * x + b)
    plt.plot(x, y)
    plt.show()


def use_stats():
    yy = y.reshape(-1, 1)
    xx = x.reshape(-1, 1)
    xx = sm.add_constant(xx)  # 如果有截距，必须有这一步骤
    model = sm.OLS(yy, xx)
    model = model.fit()
    yyy = model.predict()
    print(model.summary())
    plt.plot(x, y)
    plt.plot(x, yyy.reshape(-1))
    plt.show()


def use_sklearn():
    xx, yy = x.reshape(-1, 1), y.reshape(-1, 1)
    model = LinearRegression()
    model.fit(xx, yy)
    score = model.score(xx, yy)
    k = model.coef_[0]
    b = model.intercept_[0]
    print(f"score={score} k={k} b={b}")
    plt.plot(x, y)
    plt.plot(x, k * x + b)
    plt.show()


def use_scipy_leastsq():
    from scipy.optimize import leastsq

    def f(x, p):
        k, b = p
        return k * x + b

    def residual(p, y, x):
        return y - f(x, p)

    p0 = np.array(0.1, 0.2)
    ans = leastsq(residual, p0, args=(y, x))
    print(ans)
    plt.plot(x, y)
    plt.plot(x, f(x, ans[0]))
    plt.show()


def use_pytorch():
    import torch as t
    xx = t.tensor(x)
    yy = t.tensor(y)
    p = t.rand(2, dtype=t.float64)
    p.requires_grad = True
    opt = t.optim.Adam([p], lr=0.01)
    loss_f = t.nn.MSELoss()
    times = 0
    last_loss = 1e9
    while 1:
        yyy = p[0] * xx + p[1]
        loss = loss_f(yyy, yy)
        opt.zero_grad()
        loss.backward()
        opt.step()
        times += 1
        if times % 100 == 0:
            print(f"times={times} loss={loss}")
        if times > 1000 and abs(last_loss - loss) < 1e-4:
            break
        if times > 10000:
            break
    k, b = p.detach().numpy()
    mine = k * x + b
    plt.plot(x, y)
    plt.plot(x, mine)
    plt.show()


def use_self():
    # 手写高斯分布
    def linregress(x: np.ndarray, y: np.ndarray):
        TINY = 1.0e-20
        n = len(x)
        xmean = np.mean(x, None)
        ymean = np.mean(y, None)

        # average sum of squares:
        ssxm, ssxym, ssyxm, ssym = np.cov(x, y, bias=True).flat
        r_num = ssxym
        r_den = np.sqrt(ssxm * ssym)
        if r_den == 0.0:
            r = 0.0
        else:
            r = r_num / r_den
            # test for numerical error propagation
            if r > 1.0:
                r = 1.0
            elif r < -1.0:
                r = -1.0

        df = n - 2
        slope = r_num / ssxm
        intercept = ymean - slope * xmean
        if n == 2:
            # handle case when only two points are passed in
            if y[0] == y[1]:
                prob = 1.0
            else:
                prob = 0.0
            sterrest = 0.0
        else:
            t = r * np.sqrt(df / ((1.0 - r + TINY) * (1.0 + r + TINY)))
            prob = 2 * st.t.sf(np.abs(t), df)
            sterrest = np.sqrt((1 - r ** 2) * ssym / ssxm / df)

        return slope, intercept, r, prob, sterrest

    ###########
    k, b, r, p, sigma = linregress(x, y)
    plt.plot(x, k * x + b)
    plt.plot(x, y)
    plt.show()


# use_stats()
# use_sklearn()
# use_scipy_leastsq()
# use_pytorch()
# use_scipy()
use_self()
