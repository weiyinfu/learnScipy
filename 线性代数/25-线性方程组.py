import numpy as np
import scipy.linalg as l

a = [[1, 2], [3, 4]]
b = [5, 6]
x = np.linalg.solve(a, b)
print(np.array(a).dot(x), b)

x = l.solve(a, b)
print(np.array(a).dot(x), b)
