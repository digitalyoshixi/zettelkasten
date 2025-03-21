---
tags:
  - math
  - linalg
---
# Theorem
- Suppose $T : V\to V$ is a linear map of an $n-dim$ $\mathbb{R}$ vector space.
- Suppose $p(T) = Z$ for some polynomial $p \in P_{n}(\mathbb{R})$
- Then, factors as $Z = T^{n+n} + \dots + a_{1}T^{1} + a_{0}I = (T - \lambda_{k}I)\dots(T-\lambda_{1}I)$
- For any non-zero vector $v \in V$, we have that one of the vectors $(T - \lambda I)v,  (T- \lambda_{2}I)(T - \lambda_{1}I)v, \dots, (T - \lambda_{k-1}I)\dots(T-\lambda_{1}I)v$ is an [[Eigenvector]] of $T$