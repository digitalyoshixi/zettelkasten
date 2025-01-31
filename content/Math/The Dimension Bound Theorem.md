---
tags:
  - math
  - linalg
---
Spanning controls independence
1. If $V$ has a spanning set $T = \{ y_1, \dots, y_k\}$
2. If $S = \{ x_1, \dots, x_n\}$ is a linearly independent set
3. Then, $n \leq k$
# Proof
### Intuition
Suppose $k > n$ represent $x_i$ using $y_j$ to create a [[Homogenous Systems]]
# Proof
1. Every $x_i$ can be represented using $span(T)$
2. This means $\vec{x_i} = a_{i1}\vec{y}_1 + \dots + a_{ik}\vec{y}_k$
3. Consider $b_1\vec{x}_1 + \dots + b_x\vec{x}_n = \vec{0}$
4. This gives:
$$
\begin{align*}
\text{} & b_1(a_{11}\vec{y}_1 + \dots + a_{1k}\vec{y}_k)\\
\text{} & +\vdots\\
\text{} &+ b_n(a_{n1}\vec{y}_1 + \dots + a_{nk}\vec{y}_k) = \vec{0}\\
\end{align*}
$$
As we know that each of ${x_1, \dots, x_n}$ is linearly independent, we can say that the only way for them to be zero is if $b_1 = \dots = b_n = 0$