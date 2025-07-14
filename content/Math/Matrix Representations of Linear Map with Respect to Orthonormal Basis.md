---
tags:
  - math
  - linalg
aliases:
  - Matrix Representation from Inner Product
---
# Theorem
1. Let $T \in \mathcal{L}(v)$
2. Suppose $\beta = \{ \alpha_{1},\dots,\alpha_{n} \}$ is an ordered [[Orthonormal Set|Orthonormal Basis]] for $V$
3. Let $A = [T]_{\beta} = A_{kj}$ where $1 \leq k,j \leq n$
4. Then, $A_{kj} := \langle T\alpha_{i} | \alpha_{k \rangle}$
# Example
With $T(x,y) = (x+y,x-y)$
With [[Standard Inner Product for Real Numbers|Dot Product]]
With basis $\{ e_{1},e_{2} \}$
Then, $$[T] = \left[\begin{array}{cc} 
\langle T e_{1} | e_{2} \rangle & \langle T e_{2} | e_{1} \rangle\\
\langle T e_{2} | e_{1} \rangle & \langle T e_{2} | e_{2} \rangle\\
\end{array}\right]
= \left[\begin{array}{cc} \\
\langle 1 | 1 \rangle & \langle 1 | -1 \rangle
\end{array}\right]
$$
