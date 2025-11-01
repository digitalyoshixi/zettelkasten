---
tags:
  - math
  - calculus
---
# Example
- Suppose $R$ is a rectangle 
- Suppose $f(x,y)$ is [[Definite Integral|Integrable]] and [[Bounded Function]] $|f(x,y)| \leq M$ on $R$
- Note that this means $-M Area(R) \leq \int \int_{R} f(x)dA \leq M Area(R)$
# Proving Bounded
Pick the [[Riemann Partition]] with $N$ sub-rectangles
For upper bound:
$$\sum_{i,j=0}^{N-1}f(c_{ij}) \triangle x_{i} \triangle y_{i}$$

$$ < \sum_{i,j=0}^{N-1}f M \triangle x_{i} \triangle y_{i}$$
$$ = M \sum_{i,j=0}^{N-1}f  \triangle x_{i} \triangle y_{i}$$
$$ = M Area(R)$$
The lower bound is similar
$$\sum_{i,j=0}^{N-1}f(c_{ij}) \triangle x_{i} \triangle y_{i}$$
$$ > \sum_{i,j=0}^{N-1}f -M \triangle x_{i} \triangle y_{i}$$
$$ = -M \sum_{i,j=0}^{N-1}f \triangle x_{i} \triangle y_{i}$$
$$ = -M Area(R)$$