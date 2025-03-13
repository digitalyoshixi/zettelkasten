---
tags:
  - math
  - calculus
---
An alternate definition for [[Converging Series|Convergence]].
# Definition
- With sequence $\{ a_{n} \}_{1}^{\infty}$ be a convergent sequence given s.t $a_{n} \to L$
$\forall \epsilon > 0, \exists N > 0, \forall n,m \in \mathbb{Z}^{+}, n,m > N \implies |a_{n} - a_{m}| < \epsilon$
# Intuition
A sequence will get closer and closer to itself
# Proof of Its Equivalent to the Limit Definition
- Let $\epsilon > 0$ be arbitrary
- By defn of convergent, $\exists N \in Z^{+}, \forall n \in \mathbb{Z}^{+}, n > N \implies |a - L| < []$
- Let $n,m \in \mathbb{Z}^{+}$ be aribtrary
- Consider $|a_{n} - a_{m}| = |a_{n} -a_{m} + L - L|$
- $= |(a_{n} - L) + (L- a_{m})|$ by alg
- $\leq |a_{n} - L | + | L - a_{m}|$ by [[Triangle Inequality]]
- $= |a_{n} - L| + |a_{m} - L|$ by $| \cdot |$