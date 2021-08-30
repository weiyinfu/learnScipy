import numpy as np

a = [[1, 2], [3, 4]]
b = [5, 6]
x = np.linalg.solve(a, b)
print(np.matrix(a).dot(x), b)

import 学习scipy.linalg as l

x = l.solve(a, b)
print(np.matrix(a).dot(x), b)
