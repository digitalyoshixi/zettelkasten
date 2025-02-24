---
tags:
  - algorithm
aliases:
  - Computational Complexity
---
Describes how an algorithm performs as its input size grows infinitely large.
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
1. [[Constant Time]]
2. [[Logarithmic Time]]
3. [[Superlinear Time]]
4. [[Linear Time]]
5. [[Polynomial Time]]
6. [[Exponential Time]]
7. [[Factorial Time]]
8. [[Sublinear Time]]
- [[Inverse Ackermann Function]]
