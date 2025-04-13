---
tags:
  - math
  - calculus
aliases:
  - MS
---
# Definition
A [[Taylor Series]] at $a = 0$ for $f$.
# Formal Definition
$\sum_{n=1}^{\infty} \frac{f^{n}(0)}{n!}(x-0)^{n}$ is a maclaurin series
# Example
Compute the MS for $f(x) = e^{x}$
### Soln
1. $\sum_{n=1}^{\infty}f^{n}(0)x^{n}$ by defn of MS
2. We know that $f^{n}(x) = e^{x}$ so, $f^{n}(0) = 1$ by defn of $e^{x}$
3. Thus, $\sum_{n=1}^{\infty} \frac{x^{n}}{n!}$ is our MS for $f(x) = e^{x}$