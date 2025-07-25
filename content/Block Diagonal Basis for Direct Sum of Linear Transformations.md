---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $T$ can be written as a [[Direct Sum of Linear Transformations]] $T_{1} \oplus \dots \oplus T_{k}$
- Then, there exists a basis $\beta$ such that $[T]_{\beta}$ is [[Block Diagonal Matrix|Block Diagonal]]
# Proof
1. Suppose $T$ can be written as a direct sum $T_{1} \oplus \dots \oplus T_{k}$
2. Then, $V = W_{1} \oplus \dots \oplus W_{k}$ such that $T_{i}$ is [[Invariant]] on $W_{i}$
3. let $\beta_{i}$ be a basis for $W_{i}$ and $\beta = \bigcup_{i=1}^{k}\beta_{1}$
