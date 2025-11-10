---
tags:
  - math
  - calculus
---
# Definition
$$\int \int_{A} f(x,y)dA = \lim_{ N \to \infty } \sum_{i=1}^{N-1} \sum_{j=1}^{N-1}f(c_{ij})\triangle x \triangle y$$
- For a integral on [[Domain|Region]] $R = [a,b] \times[c,d]$
- The partitions will be:
	- $\{ x_{i}^{*} \}, a =x_{0}<x_{1} < \dots <x_{N} = b$
	- $\{ y_{i}^{*}  \},  c = y_{0} < \dots <y_{N} = d$
- The sample points are the 2d vectors $c_{ij} \in [x_{i},x_{i+1}] \times [y_{i},y_{i+1}]$