---
tags:
  - math
  - statistics
  - probability
---
# Definition
Uniform RV $X$ takes values in interval $[l,u], l<u\in\mathbb{R}$ s.t probability of any subinterval is proportional to its length:
$$P(a < X < b) = \frac{b-a}{u-l}, \forall l \leq a \leq b \leq u$$
# PDF Requirement
$$f_{X}(x) =
\begin{cases}
\frac{1}{u-l} & 1 \leq x \leq u\\
0 & \text{otherwise}\\
\end{cases}
$$
![[Uniform Random Variable-20250930141752842.webp]]
# CDF Requirement
$$F(x) =
\begin{cases} \\
0 & x < 1\\
\frac{x-l}{u-l} & 1 \leq x \leq u\\
1 & x > u\\
\end{cases}
$$
![[Uniform Random Variable-20250930141801235.webp]]