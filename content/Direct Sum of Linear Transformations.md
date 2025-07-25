---
tags:
  - math
  - linalg
---
# Definition
- Suppose $T \in \mathcal{L}(V)$ 
- Suppose $V = W_{1} \oplus .. \oplus W_{k}$ where each $W_{i}$ is [[Invariant]]
- let $T_{j}$ be the restriction of $T$ to $W_{j}$
- As $V$ is a direct sum, then every vector $\alpha \in V$ is represented uniquely by vectors in $W_{1} , \dots, W_{k}$. That is to say, $\forall \alpha, \alpha_{1} + \dots \alpha_{k} \in V$
- Applying to $T$ gives: $T(\alpha) = T(\alpha_{1} + \dots + \alpha_{k}) = T(\alpha_{1}) + \dots + T_{k}(\alpha_{k})$
- Then, we say that $T$ is the direct sum of $T_{j} \in L(W_{j})$ and write $T = T_{1} \oplus \dots \oplus T_{k}$
# Theorems
- [[Block Diagonal Basis for Direct Sum of Linear Transformations]]
- [[Invariant Direct Sum of Linear Transformations Theorem]]