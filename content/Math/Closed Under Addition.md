---
tags:
  - math
  - linalg
---
A set is closed under addition if the sum of two elements in a set is also a member of the same set.
$$\vec{x},\vec{y} \in S \implies \vec{x}+\vec{y} \in S$$
# Examples
The set $P = \{ (x,y,z) \in R^3 ;z = 0\}$
Is closed under addition. We can verify this by:
- $(x_{1},y_{1},0)$ and $(x_{2}, y_{2}, 0)$  have a sum $(x_{1}+x_{2}, y_{1}+y_{2},0)$ which is in $P$
The set $P = \{ (x,y,z) \in R^3 ;z = 1\}$
Is **not** closed under addition.
- $(1,1,1)$ and $2,1,1$ are in $P$, but $(1,1,1) + (2,1,1) = (3,3,2)$ which is not in $P$.
# Proving Closed Under Addition Example
![[Closed Under Addition-20250109000910209.webp]]