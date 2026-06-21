---
tags:
  - programming
  - math
---
A optimization after [[Lattice Joining]], over-approximates to find [[Series Convergence]]. It is an function $\triangledown: L \times L \to L$ that takes $\triangledown(L_{previous}, L_{current}) = L_{new}$
# Process
With intervals $[a,b] \triangledown [c,d]$:
- New lower bound is $-\infty$ if $c < a$
- New upper bound is $\infty$ if $d > b$
# Widening Techniques
- [[Delay Widening]]