---
tags:
  - algorithm
aliases:
  - Time Complexity
  - Space Complexity
  - Big Oh Notation
---
Describes an upper bound for an algorithm as its input size grows infinitely large with a chosen unit of measurement.
- Denoted as $O(g(x))$ with $g(x)$ being the smallest growing function such that $f(n) < c * O(n)$
![[big-o-chart-3693586841.png]]
![[Big O Notation-20250420022901850.webp]]
# Complexity Notation
$O(g(N))$ is the family of all functions $f(N)$ such that:
$\exists c, \lim_{ n \to \infty } f(N) \leq \lim_{ n \to \infty } c * g(N)$
- Or in other words, $c * g(N)$ is always an upper bound of $f(N)$ as $n\to \infty$
### Formal Definition
Let $g \in \mathcal{}F$ define $O(g)$ to be the set of functions $f \in \mathcal{F}$ s.t
$\exists b \in \mathbb{R}^{+}, \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N}, n > n_{0} \implies f(n) \leq b \cdot g(n) \geq 0$
##### Intuition
A function $f(n) \in O(g(n))$ if the following conditions hold:
- $\exists n_0 \in \mathbb{N}$
- $\exists c\in \mathbb{R}$
Such that: $0 \leq f(n) \leq c \cdot g(n)$ when $n > n_{0}$
### Big O Notation Simplification
Remove all coefficients and constants.
- O(2n) -> O(n)
- O(2+log(n)/2) -> O(log n)
- O(4) -> O(1)
# Complexities (Ranked)
1. [[Constant Time]]
2. [[Logarithmic Time]]
3. [[Sublinear Time]]
4. [[Linear Time]]
5. [[Superlinear Time]]
6. [[Polynomial Time]]
7. [[Exponential Time]]
8. [[Factorial Time]]
9. [[Inverse Ackermann Function]]
