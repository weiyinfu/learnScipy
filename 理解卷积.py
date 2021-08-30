def convolve(a, b):
    c = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c


a = [1, 2, 3]
b = [4, 5, 6]
print(convolve(a, b))
import numpy as np
print(np.convolve(a, b))
