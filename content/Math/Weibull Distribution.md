---
tags:
  - statistics
---
Used to model failure time between events.
![[Weibull Distribution-20251011000232205.webp]]
# CDF
$$
F(t) = \begin{cases}
1 - e^{-(\lambda t)^{k}} & t \geq 0\\
0 & t < 0
\end{cases}
$$
Where:
- $\lambda>0$ is the rate parameter
- $k > 0$ is the shape parameter
