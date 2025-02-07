---
tags:
  - linalg
  - math
---
Let $V$, $W$ be finite dimensional vector spaces with $dim(V) = n$ and $dim(W) = k$

Any linear transformation $T: V\to W$ is uniquely identified by $nk$ scalars.

# Intuition
Fix bases $\alpha = \{ v_{1}, \dots , v_{n} \}$
$\beta = \{ w_{1}, \dots, w_{n} \}$
With $V =span(\alpha)$
$W = span(\beta)$
# Proof
We know that $T$ is uniquely [[Linear Maps Determined by Their Actions on A Basis|determined by their actions on a basis]].
Thus, we have $T(v_{i}) \subset W$
$\implies T(v_{1}) = a_{11}\overrightarrow{w_{1}} + .. + a_{1k}\overrightarrow{w_{k}}$
$\vdots$
$T(v_{n}) = a_{n1} \overrightarrow{w_{1}} + \dots + a_{nk}\overrightarrow{w_{k}}$
then, there are $nk = dim(V) * dim(W)$ amount of coefficients with determine the map $T : V\to W$.

