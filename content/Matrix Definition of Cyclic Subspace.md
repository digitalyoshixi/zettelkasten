---
tags:
  - math
  - linalg
aliases:
  - Companion Matrix
---
# Theorem
- Let $V$ as a vector space
- Let $\alpha \in V$
- With $T \in \mathcal{L}(V)$
- Then $p(x) = x^{n} + a_{n-1}x^{n-1} + \dots + a_{1}x +a_{0}$ be the $T$-annihilator of $\alpha$
- With $\beta = \{  \alpha, T \alpha, \dots, T^{n-1}\alpha \}$ as a basis for $Z(\alpha_{i}T)$  be the linear operator defined by restriction of $T$ onto the subspace $Z(\alpha_{i}T)$ then,
- $$
 [T_{Z}]_{\beta} =  \left[\begin{array}{cc}
0 & 0 & 0 & \dots & 0 & - \alpha_{0}\\
1 & 0 & 0 & \dots & 0 & -\alpha_{1}\\
0 & 1 & 0 & \dots & 0 & - \alpha_{2}\\
\vdots & \vdots & \ddots & \ddots & 0 & -\alpha_{z}\\
0 & 0 & 0 & \dots & 1 & -\alpha_{z-1}\\
\end{array}\right]
  $$

# Example
Find companion matrix for $x^{3} -5x + 8x - 4$
1. We write the first columns out
   $$
   \left[\begin{array}{ccc}
0 & 0 & ?\\
1 & 0 & ?\\
0 & 1 & ?\\
\end{array}\right]
   $$
2. The last column is the negative versions of our coefficients
   $$
   \left[\begin{array}{ccc}
0 & 0 & 4\\
1 & 0 & -8\\
0 & 1 & 5\\
\end{array}\right]
   $$