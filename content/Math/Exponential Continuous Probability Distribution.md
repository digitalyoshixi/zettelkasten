---
tags:
  - math
  - statistics
  - probability
---
Exponential RV $X$ takes positive values according to PDF:
# PDF
$$
f(x,\lambda) = \begin{cases}
\lambda e^{-\lambda x} & x \geq 0\\
0 & x < 0\\
\end{cases}
$$
For some $\lambda > 0$
# CDF
$$
F(x,\lambda) = \begin{cases}
1-e^{-\lambda x} & x \geq 0 \\
0 & x < 0
\end{cases}
$$
![[Exponential Continuous Probability Distribution-20250930142027244.webp]]
# [[Expectation]]
$$E(X) = \frac{1}{\lambda}$$
# [[Variance]]
$$
\frac{1}{\lambda^{2}}
$$
# [[Moment Generating Function|MGF]]
$$
\frac{\lambda}{\lambda - t} , t < \lambda
$$
