---
tags:
  - math
  - statistics
---
# Theorem
- For $X_{1},\dots,X_{n} \sim_{iid} N(\mu, \sigma^2)$
- $U$ and $V$ are two different linear combinations of $X_{i}$s
- $cov[U,V] = 0 \Longleftrightarrow U \bot V$
# Linear Combinations
- Say $i = 1$
- Then,  $U = \overline x = \frac{1}{n}x_{1} + \frac{1}{n}x_{2} +\dots+\frac{1}{n}x_{n}$
- Then,  $V = x_{i} - \overline x= x_{1}-\frac{1}{n}x_{1} + x_{2}-\frac{1}{n}x_{2} +\dots+x_{n}-\frac{1}{n}x_{n}$
- Then, we get $cov[\overline x, x_{i} - \overline x]$
- $cov[\overline x, x_{i}] -  cov[\overline x, \overline x]$
- $\frac{1}{n}cov[x_{1},x_{1}] + \frac{1}{n}cov[x_{2},x_{1}] + \dots - V[\overline x]$
- $= \frac{1}{n}V[x_{i}] - V[\overline x]$
- $= \frac{1}{n}\sigma^{2} - \frac{\sigma^{2}}{n} = 0$
Therefore, $\overline X \bot X_{i} - \overline X, \text{ for } i=1,2,\dots,n$