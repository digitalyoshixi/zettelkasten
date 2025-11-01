---
tags:
  - math
  - statistics
aliases:
  - Sum of RV
---
# Definition
- With [[Random Variable|RV]] $X,Y$
- The sum of RVs $Z = X+Y$ is a [[Functions of Random Variables|Transformation]]
[[Cumulative Distribution Function|CDF]] of $Z$ is is:
$$F_{Z}(z) = P(Z \leq z) = P(X+Y \leq z)$$
$$P(Y \leq z-X) = 
\begin{cases}
\int\int_{R} f_{X,Y}(x,y)dxdy\\ 
\sum\sum_{R}p_{X,Y}(x,y)
\end{cases}
$$
# Concepts
- [[Convolution Method]]