import scipy.stats as st

"""
在scipy.stats这个包中，经常见到一堆arg1，arg2....  
很多函数都是既包含args，又包含kwargs。那么这些参数是什么意思呢？  
sf(self, x, *args, **kwds)

查看一下文档：  
  arg1, arg2, arg3,... : array_like
            The shape parameter(s) for the distribution (see docstring of the
            instance object for more information)

文档也是不清不楚，意思是让我去看具体实例的文档来查找更多信息            

实际上，scipy.stats这个文件定义了随机变量rv这个东西，有派生出连续型随机变量和离散型随机变量。
为了让各种分布有统一的接口，scipy.stats各个分布的函数参数形状为(x,*args,**kwargs)
"""
print(st.t.sf(3, 2))
print(st.t.sf(3, df=2))
print(st.t.sf(3, df=2, loc=0, scale=1))
print(st.t.sf(3, 2, 0, 1))
