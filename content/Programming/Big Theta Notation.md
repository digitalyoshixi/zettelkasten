---
tags:
  - programming
aliases:
  - Asymptotic Tight Bound
---
An alternate to [[Big O Notation]] that only covers worst-case scenario.
# Definition
Let $g \in \mathcal{F}$, then define $\Theta(g)$ to be the set of all functions $f \in \mathcal{F}$ s.t $f \in O(g) \cap \Omega(g)$
Alternatively,
$\exists b \in \mathbb{R}^{+}, \exists c \in \mathbb{R}^{+}, \exists n_0 \in \mathbb{N}, \forall n \in \mathbb{N}, n > n_{0} \implies 0 \leq b \cdot g(n) \leq f(n) \leq c \cdot g(n)$
# Intuition
Given $\theta(g(N))$, this means that for a given function $g(x)$, there are two constants $c_{1},c_{2}$ s.t $c_{1}g(x) \geq f(x) \geq c_{2}g(x)$ that match the actual function of the argument $f(x)$.
