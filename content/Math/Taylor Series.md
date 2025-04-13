---
tags:
  - math
  - calculus
aliases:
  - TS
---
A method of expressing a function as a [[Power Series]] of that function's derivatives.
# Formal Definition
- For a given function $f(x)$
- Considering power series $\sum_{n=1}^{\infty} C_{n}(x-a)^{n}$
- Note $C_{n} = \frac{f^{n}(a)}{n!}$ for any $n$ ($f^{n}$ being the n-th derivative)
- Then, $f(x) = \sum_{n=1}^{\infty} \frac{f^{n}(a)}{n!}(x-a)^{n}$ is a Taylor series for $f$ at $a$
# Intuition
![[Taylor Series-20250413042919202.webp|434]]
# Concepts
- [[Maclaurin Series]]