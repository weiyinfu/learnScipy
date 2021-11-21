scipy.optimize是scipy下面最有用的包，包含的内容是最为神奇玄妙的。
* nonlinear problems (with support for both local and global optimization algorithms)
* linear programing
* constrained and nonlinear least-squares
* root finding
* curve fitting.  

覆盖的学科包括：运筹学、最优化、求根、曲线拟合。  

# 优化
## 单变量优化
最小化只包含一个参数的函数。    
支持的方法包括：
* minimize_scalar(method=’brent’)
* minimize_scalar(method=’bounded’)
* minimize_scalar(method=’golden’)

## 多变量局部优化
* minimize(method=’Nelder-Mead’)
* minimize(method=’Powell’)
* minimize(method=’CG’)
* minimize(method=’BFGS’)
* minimize(method=’Newton-CG’)
* minimize(method=’L-BFGS-B’)
* minimize(method=’TNC’)
* minimize(method=’COBYLA’)
* minimize(method=’SLSQP’)
* minimize(method=’trust-constr’)
* minimize(method=’dogleg’)
* minimize(method=’trust-ncg’)
* minimize(method=’trust-krylov’)
* minimize(method=’trust-exact’)

Constraints are passed to minimize function as a single object or as a list of objects from the following classes:

NonlinearConstraint(fun, lb, ub[, jac, …])

Nonlinear constraint on the variables.

LinearConstraint(A, lb, ub[, keep_feasible])

Linear constraint on the variables.

Simple bound constraints are handled separately and there is a special class for them:

Bounds(lb, ub[, keep_feasible])

Bounds constraint on the variables.

Quasi-Newton strategies implementing HessianUpdateStrategy interface can be used to approximate the Hessian in minimize function (available only for the ‘trust-constr’ method). Available quasi-Newton methods implementing this interface are:

BFGS([exception_strategy, min_curvature, …])

Broyden-Fletcher-Goldfarb-Shanno (BFGS) Hessian update strategy.

SR1([min_denominator, init_scale])

Symmetric-rank-1 Hessian update strategy.
## 单变量全局优化 
* `basinhopping(func, x0[, niter, T, stepsize, …])`
Find the global minimum of a function using the basin-hopping algorithm.

* `brute(func, ranges[, args, Ns, full_output, …])`

Minimize a function over a given range by brute force.

* `differential_evolution(func, bounds[, args, …])`

Finds the global minimum of a multivariate function.

* `shgo(func, bounds[, args, constraints, n, …])`

Finds the global minimum of a function using SHG optimization.

* `dual_annealing(func, bounds[, args, …])`
双模拟淬火 
Find the global minimum of a function using Dual Annealing.

# 最小二乘和曲线拟合
## 最小二乘法
least_squares(fun, x0[, jac, bounds, …])
## 带约束的最小二乘法
Linear least-squares
`nnls(A, b[, maxiter])`

Solve `argmin_x || Ax - b ||_2 for x>=0`.

`lsq_linear(A, b[, bounds, method, tol, …])`
## Curve fitting
曲线拟合本身也是基于最小二乘法进行曲线拟合。  
`curve_fit(f, xdata, ydata[, p0, sigma, …])`

Use non-linear least squares to fit a function, f, to data.

# 求根
## 一元函数求根
The root_scalar function supports the following methods:

root_scalar(method=’brentq’)
root_scalar(method=’brenth’)
root_scalar(method=’bisect’)
root_scalar(method=’ridder’)
root_scalar(method=’newton’)
root_scalar(method=’toms748’)
root_scalar(method=’secant’)
root_scalar(method=’halley’)

fixed_point(func, x0[, args, xtol, maxiter, …])

Find a fixed point of the function.
## 多元函数求根
root(fun, x0[, args, method, jac, tol, …])

Find a root of a vector function.

The root function supports the following methods:

root(method=’hybr’)
root(method=’lm’)
root(method=’broyden1’)
root(method=’broyden2’)
root(method=’anderson’)
root(method=’linearmixing’)
root(method=’diagbroyden’)
root(method=’excitingmixing’)
root(method=’krylov’)
root(method=’df-sane’)
# 线性规划
`linprog(c[, A_ub, b_ub, A_eq, b_eq, bounds, …])`

Linear programming: minimize a linear objective function subject to linear equality and inequality constraints.

The linprog function supports the following methods:

linprog(method=’simplex’)
linprog(method=’interior-point’)
linprog(method=’revised simplex’)
linprog(method=’highs-ipm’)
linprog(method=’highs-ds’)
linprog(method=’highs’)
The simplex, interior-point, and revised simplex methods support callback functions, such as:

linprog_verbose_callback(res)

A sample callback function demonstrating the linprog callback interface.
# 分配问题
`linear_sum_assignment(cost_matrix[, maximize])`

Solve the linear sum assignment problem.

`quadratic_assignment(A, B[, method, options])`

Approximates solution to the quadratic assignment problem and the graph matching problem.

The quadratic_assignment function supports the following methods:

quadratic_assignment(method=’faq’)
quadratic_assignment(method=’2opt’)
# 工具函数
## 有限差分近似 Finite-difference approximation
## 线性搜索Line search
## hessian近似 Hessian approximation
## 基准问题
https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume24/ortizboyer05a-html/node6.html


# legacy函数
scipy.optimize下的函数以前是每种方法都是一个独立的函数，这样做的好处是可以为不同的方法指定不同的超参数。  
现在新版的函数变成了method+options形式，使得函数的个数大幅下降。  