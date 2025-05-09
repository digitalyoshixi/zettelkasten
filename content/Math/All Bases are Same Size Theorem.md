---
tags:
  - linalg
  - math
aliases:
  - Invariance Theorem
---
If $S = \{ x_{1},\dots,x_{k} \}$ and $S' = \{ y_{1}, \dots, y_{n} \}$ are two finite bases of [[Vector Space]] $V$, then $n = k$.

This means that all bases are the same size.
![[Invariance Theorem-20250125164100552.webp]]
Allows for the [[Vector Space Dimension]] function
# Proof
Case 1:
Consider $S$ as the spanning set
Consider $S'$ as the indep set.
Then: $n \leq k$ by [[The Dimension Bound Theorem]].

Case 2:
Consider $S'$ as the spanning set
Consider $S$ as the independent set
This gives $k \leq n$ again by [[The Dimension Bound Theorem]]
Therefore, $n = k$
$$\square$$