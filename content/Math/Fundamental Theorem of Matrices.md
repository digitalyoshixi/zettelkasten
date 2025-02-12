---
tags:
  - math
  - linalg
---
1. If $M \in M_{n \times k}(\mathbb{R})$ then, $T_{M}$ is a linear transformation
2. If $T : V\to W$ has matrix $M = [T]_{\alpha}^{\beta}$ then $T = T_{M}$
3. If $M \in M_{n \times k}(\mathbb{R})$ then $M = [T_{m}]_{\alpha}^{\beta}$
![[Fundamental Theorem of Matrices-20250212143632302.webp]]

# Example Utilization
1. $T(x,y,z) = (x+y+z,y+x,z)$
2. $T(1,2,3)$
Solution:
1. $T(1,2,3) = [6,3,3]$
Verify other side
1. Find $[T]_{\alpha}^{\alpha}$
2. $T(1,0,0) = (1,1,0)$
3. $T(0,1,0) = (1,1,0)$
4. $T(0,0,1) = (0,0,1)$
5. Then, $$[T]_{\alpha}^{\alpha} = 
\left[\begin{array}{ccc}
1 & 1 & 1\\
1 & 1 & 0\\
0 & 0 & 1\\
\end{array}\right]
$$
6. Then, $$[T]_{\alpha}^{\alpha}[(1,2,3)] = 
\left[\begin{array}{ccc}
1 & 2 & 3\\
1 & 2 & 0\\
0 & 0 & 3\\
\end{array}\right] = [6,3,3]
$$
Thus, they are equal