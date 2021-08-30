from scipy.optimize import fsolve,leastsq
from math import sin,cos
 
def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2-1.5
        ]
 
x0 = [1,1,1]
result = fsolve(f,x0)
 
print("===================")
print()
print("求解函数名称:",fsolve.__name__)
print("解：",result)
print("各向量值：",f(result))
#拟合函数来求解
h = leastsq(f,x0)
 
print("===================")
print()
print("求解函数名称:",leastsq.__name__)
print("解：",h[0])
print("各向量的值：",f(h[0]))
