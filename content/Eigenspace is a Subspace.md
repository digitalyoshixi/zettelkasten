---
tags:
  - math
  - linalg
---
# Theorem
For any $\lambda \in \mathbb{R}$, we have $E_{\lambda}$ is a subspace of $V$
# Proof
1. Check that $E_{\lambda}$ is non-empty
2. Note that we have $T(0)= \overrightarrow{0} = \lambda 0$
3. Thus, $\overrightarrow{0} \in E_{\lambda}$ for any $\lambda \in \mathbb{R}$
4. Note that $0$ is not an [[Eigenvector]], but it is in $E_{\lambda}$
5. Pick $x,y \in E_{\lambda}$, and $c \in \mathbb{R}$
6. Then, we get: $T(cx+y)$
7. $= cT(x) + T(y)$
8. $= c(\lambda x) + \lambda y$
9. $= \lambda(cx+y)$
10. Thus, $cx+y \in E_{\lambda}$
11. It follows that $E_{\lambda}$ is a [[Subspace]]
