from scipy import integrate

f = lambda y, x: x * y ** 2
# x从0到2
# y从f(x)到t(x)
ans = integrate.dblquad(f, 0, 2, lambda x: 0, lambda x: 1)
print(ans)
