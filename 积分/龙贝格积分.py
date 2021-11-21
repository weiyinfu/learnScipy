import numpy as np
from scipy import integrate

gaussian = lambda x: 1 / np.sqrt(np.pi) * np.exp(-x ** 2)
result = integrate.romberg(gaussian, 0, 1, show=True)
print(result)