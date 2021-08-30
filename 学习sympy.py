from sympy import *

x = Symbol('x')  # 默认x为复数
print(expand(E ** (I * x)))
print(expand(E ** (I * x), complex=True))
x = Symbol('x', real=True)  # x为实数
print(expand(E ** (I * x), complex=True))

tmp = series(exp(I * x), x, 0, 10)
pprint(tmp)
pprint(re(tmp))

print(integrate(x * sin(x), x))  # 不定积分
print(integrate(x * sin(x), (x, 0, 2 * pi)))  # 定积分

x, y, r = symbols('x,y,r')
print(2 * integrate(sqrt(r * r - x ** 2), (x, -r, r)))  # 得不到答案，因为r不知道是否大于0

r = symbols('r', positive=True)
circle_area = 2 * integrate(sqrt(r ** 2 - x ** 2), (x, -r, r))
circle_area = circle_area.subs(r, sqrt(r ** 2 - x ** 2))
print(circle_area)
"""
用subs进行算式替换

subs函数可以将算式中的符号进行替换，它有3种调用方式：

expression.subs(x, y) : 将算式中的x替换成y
expression.subs({x:y,u:v}) : 使用字典进行多次替换
expression.subs([(x,y),(u,v)]) : 使用列表进行多次替换
请注意多次替换是顺序执行的，因此：

expression.sub([(x,y),(y,x)])
并不能对两个符号x,y进行交换。
"""
print(integrate(circle_area, (x, -r, r)))
