---
tags:
  - math
aliases:
  - Least Squares Solution
---
![[Least Squares Method-20231221130848865.webp]]
# Least Square Solution Definition
- If $A$ is a $m \times n$ matrix,
- $b \in \mathbb{R}^{m}$
- a least square solution of $Ax = b$ is a vector $\hat{x} \in \mathbb{R}^{n}$ such that:
- $|| b - A \hat{x} || \leq || b - A x ||, \forall x \in \mathbb{R}^{n}$ ([[Best Approximation]])
You can find $x$ with [[Least Squares Theorem]]
# Intuition
- With an error vector $e$
- We reduce the error by finding the smallest $e$ (least square) for $||e||^{2} = \langle e | e \rangle$
- With $$c = \left[\begin{array}{cc}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right]$$
- With $$A = \left[\begin{array}{cc}
1 & x_{1} \\
1 & x_{2} \\
\vdots \\
1 & x_{n}
\end{array}\right]$$
- The vector $e = c - Ax$
