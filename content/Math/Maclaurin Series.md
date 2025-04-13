---
tags:
  - math
  - calculus
aliases:
  - MS
---
A way of representing a function as a [[Power Series]]. It is a [[Taylor Series]] at $a = 0$ for $f$.
# Formal Definition
$f(x) = \sum_{n=1}^{\infty} \frac{f^{n}(0)}{n!}(x-0)^{n}$ is a maclaurin series representation of $f$
# Example
Compute the MS for $f(x) = e^{x}$
### Soln
1. $\sum_{n=1}^{\infty}f^{n}(0)x^{n}$ by defn of MS
2. We know that $f^{n}(x) = e^{x}$ so, $f^{n}(0) = 1$ by defn of $e^{x}$
3. Thus, $\sum_{n=1}^{\infty} \frac{x^{n}}{n!}$ is our MS for $f(x) = e^{x}$