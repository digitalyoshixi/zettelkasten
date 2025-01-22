---
tags:
  - calculus
---
### Integration By Parts (The Worst Technique)
Differentiate a function that is the product of 2 simpler functions. It is an [[Iterative Process]]
$\int u'v \, dx = uv - \int uv' \, dx$
1. Assign $\int u'$ and $\int  v$
2. Determine $u$ and $v'$
3. Check $\int u'v \, dx = uv - \int uv' \, dx$
4. There is one $+c$ at the very end, so you dont need to have $+c$ midway.
##### Wrong Example
Determine $\int x\sin x \, dx$
1. $u' = x$, and then naturally, $v=\sin x$
2. Therefore, $u=\frac{x^2}{2}+c$ as the antiderivative of $u'$. $v' = \cos x$ 
3. Check $uv - \int uv' \, dx = \frac{x^2}{2}\sin x - \int \frac{x^2}{2} \, dx$.
	1. It is too hard to integrate $\int \frac{x^2}{2} \, dx$, therefore, this was a bad decision of $u'$ and $v$
##### Right Example
Determine $\int x\sin x \, dx$
1. $u'=\sin x$, $v=x$
2. $u = -\cos x$, $v'=1$
3. $uv - \int uv' \, dx = -x\cos x - \int (-\cos x) \, dx$
4. Now solve, $\int x\sin x \, dx= -x\cos x+\sin x+c$
