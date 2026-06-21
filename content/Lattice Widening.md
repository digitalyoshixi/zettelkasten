---
tags:
  - programming
  - math
---
A optimization after [[Lattice Joining]], over-approximates to find [[Series Convergence]]. It is an function $\triangledown: L \times L \to L$ that takes $\triangledown(L_{previous}, L_{current}) = L_{new}$
# Process
With intervals $[a,b] \triangledown [c,d]$:
$$
[a,b] \triangledown [c,d] = [a', b']
$$
With:
$$
a' = \begin{cases}
-\infty & \text{if } c < a\\
a & \text{o.w}
\end{cases}
$$
$$
b' = \begin{cases}
\infty & \text{if } d < b\\
b & \text{o.w}
\end{cases}
$$
# Widening Techniques
- [[Delay Widening]]