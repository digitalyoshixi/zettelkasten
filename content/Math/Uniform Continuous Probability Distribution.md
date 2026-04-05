---
tags:
  - math
  - statistics
  - probability
aliases:
  - Uniform Probability
---
# Definition
$X \sim \text{Uniform}(u,l)$ takes values in interval $[l,u], l<u\in\mathbb{R}$ s.t probability of any subinterval $[a,b]$ is proportional to its length:
$$P(a < X < b) = \frac{b-a}{u-l}, \forall l \leq a \leq b \leq u$$
# PDF Requirement
$$f_{X}(x) =
\begin{cases}
\frac{1}{u-l} & l \leq x \leq u\\
0 & \text{otherwise}\\
\end{cases}
$$
![[Uniform Random Variable-20250930141752842.webp]]
# CDF Requirement
$$F(x) =
\begin{cases} 
0 & x < l\\
\frac{x-l}{u-l} & l \leq x \leq u\\
1 & x > u\\
\end{cases}
$$
![[Uniform Random Variable-20250930141801235.webp]]
# Expectation
$$E(X) = \frac{u+l}{2}$$
# Variance
$$V(X) = \frac{(u-l)^{2}}{12}$$
# [[Moment Generating Function|MGF]]
$$
\frac{e^{tu}-e^{tl}}{t(u-l)}
$$
