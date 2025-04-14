---
tags:
  - math
  - calculus
aliases:
  - Geometric Series Divergence
  - GS Test
---
# GS-Test
1. Given $\sum_{n=i}^{\infty}a_{i}r^{n}$, $a_{i}, r \in \mathbb{R}, a_{i} \neq 0$ is a [[Geometric Series]]
2. If $|r| < 1$ then, $\sum a_{i}r^{n}$ converges to $\frac{a}{1-r}$
3. If $|r| \geq 1$  then, $\sum a_{i}r^{n}$ diverges
# GS Test Example
Prove $\sum_{n=4}^{\infty}((\frac{1}{2})^{n} - 7 (\frac{6}{11})^{n})$ converges
- $= \sum_{n=4}^{\infty}(\frac{1}{2})^{n} +  \sum_{n=4}^{\infty}- 7 (\frac{6}{11})^{n}$
- Note that $\sum_{n=4}^{\infty}(\frac{1}{2})^{n}$ is a [[Geometric Series]] with:
	- $a = (\frac{1}{2})^{4}$
	- $r = (\frac{1}{2})$
- Then, the series converges to $\frac{a}{1-r} = \frac{7}{5}(\frac{6^{4}}{11^{3}})$ by [[Partial Sums for Geometric Series]] formulas
- Note that $\sum_{n=4}^{\infty}- 7 (\frac{6}{11})^{n}$ is a [[Geometric Series]] with;
	- $a = -7(\frac{6}{11})^{4}$
	- $r = (\frac{6}{11})$
- Then, the series converges to $\frac{a}{1-r} = (\frac{1}{2})^{4}$ by [[Partial Sums for Geometric Series]] formulas
- Then, the entire series converges to $(\frac{1}{2})^{4} - \frac{7}{5}(\frac{6^{4}}{11^{3}})$