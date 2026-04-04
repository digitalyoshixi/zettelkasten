---
tags:
  - calculus
---
Integration technique often used for integrating:
- [[Inverse Function]]
- [[Product Functions]]
# Integration By Parts
Differentiate a function that is the product of 2 simpler functions. It is an [[Iterative Process]]
$\int uv' = uv - \int u'v$
or
$\int u\,dv = uv - \int v\,du$
Where:
- $u=f(x)$ is [[Differentiability|Differentiable]]
- $v =g(x)$ is [[Differentiability|Differentiable]]
### Solving Process
1. Pick $u$ and $dv$
	1. Usually pick $u$ as a [[Logarithm]] or [[Inverse Trigonometric Functions]] if there is one in the LHS
2. Compute $du$ and $v$
3. Check $\int u\,dv = uv - \int v\,du$
4. Remember there is one $+c$ at the very end
# Tricks
Since Integration by parts is very guess-heavy, you tend to be able to see if you are on the right track early on by your computations of $v, du$
##### Wrong Example
Determine $\int x\sin x \, dx$
5. $u' = x$, and then naturally, $v=\sin x$
6. Therefore, $u=\frac{x^2}{2}+c$ as the antiderivative of $u'$. $v' = \cos x$ 
7. Check $uv - \int uv' \, dx = \frac{x^2}{2}\sin x - \int \frac{x^2}{2} \, dx$.
	1. It is too hard to integrate $\int \frac{x^2}{2} \, dx$, therefore, this was a bad decision of $u'$ and $v$
##### Right Example
Determine $\int x\sin x \, dx$
8. $u'=\sin x$, $v=x$
9. $u = -\cos x$, $v'=1$
10. $uv - \int uv' \, dx = -x\cos x - \int (-\cos x) \, dx$
11. Now solve, $\int x\sin x \, dx= -x\cos x+\sin x+c$