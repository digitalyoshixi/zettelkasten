---
tags:
  - math
  - linalg
aliases:
  - Vector Metric
---
# Definition
- With $B$ as a [[Vector Space]]
- With $d: V \times V \to \mathbb{R}$ as a function
- The function $d$ is a metric if:
	1. $d(v,w) \geq 0, \forall v,w \in V$ (Non-negativity)
	2. $d(v,w) = d(w,v)$ ([[Commutative]]/[[Symmetric]])
	3. $d(v,w) = 0 \Longleftrightarrow v = w$ (Zero distance for equality)
	4. $d(u,w) \leq d(u,v) + d(v,w)$ ([[Triangle Inequality]])
# Implementations
- [[Euclidean Metric for Reals in R2]]
- [[1-Metric]]