---
tags:
  - algorithm
aliases:
  - Computational Complexity
---
Describes how an algorithm performs as its input size grows infinitely large.
It is the smallest growing function $g(n)$ such that $f(n) < c * g(n)$
![[big-o-chart-3693586841.png]]
# Complexity Notation
$O(g(N))$ is the family of all functions $f(N)$ such that:
$\forall c, \lim_{ n \to \infty } f(N) \leq \lim_{ n \to \infty } c * g(N)$
- Or in other words, $c * g(N)$ is always an upper bound of $f(N)$ as $n\to \infty$
### Big O Notation Simplification
Remove all coefficients and constants.
- O(2n) -> O(n)
- O(2+log(n)/2) -> O(log n)
- O(4) -> O(1)
# Complexities (Ranked)
1. [[Logarithmic Time]]
2. [[Superlinear Time]]
3. [[Sublinear Time]]
4. [[Constant Time]]
5. [[Linear Time]]
6. [[Polynomial Time]]
7. [[Exponential Time]]
8. [[Factorial Time]]
9. [[Inverse Ackermann Function]]
