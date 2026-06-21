---
tags:
  - programming
  - math
---
A optimization after [[Lattice Joining]]. It is an operation $\triangledown: L \times L \to L$ that takes all join points and over-approximates to find [[Series Convergence]].
# Process
With intervals $[a,b] \triangledown [c,d]$:
- New lower bound is $-\infty$ if $c < a$
- New upper bound is $\infty$ if $d > b$