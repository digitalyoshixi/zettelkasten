---
tags:
  - programming
---
Describes a lower bound for a given function as its input size increases to infinity.
# Definition
Let $g \in \mathcal{}F$ define $\Omega(g)$ to be the set of functions $f \in \mathcal{F}$ s.t
$\exists b \in \mathbb{R}^{+}, \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N}, n > n_{0} \implies f(n) \geq b \cdot g(n) \geq 0$

Equivalently, $f \in \Omega(g) \Longleftrightarrow g \in O(f)$