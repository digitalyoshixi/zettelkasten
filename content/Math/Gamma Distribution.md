---
tags:
  - math
  - statistics
---
A distribution of independent $Exponential(\lambda)$ values.
![[Gamma Distribution-20250930142457876.webp]]
# PDF
$$
f(x) = \begin{cases}
\frac{\lambda^{a}}{\Gamma(a)}x^{a-1}e^{-\lambda x} & x > 0\\
0  & x \leq 0\\
\end{cases}
$$
- Where $a, \lambda > 0$
- Where $\Gamma$ is the [[Gamma Function]]
- Denoted by $X \sim Gamma(a, \lambda)$
# CDF
No closed form CDF, unless $a=1$, then this is [[Exponential Continuous Probability Distribution]]
![[Gamma Distribution-20250930142841526.webp]]