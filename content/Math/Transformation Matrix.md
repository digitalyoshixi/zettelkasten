---
tags:
  - math
  - linalg
aliases:
  - Matrix Representation of Linear Transformation
---
A way of representing [[Linear Transform|Linear Map]] as a matrix.
# Theorem
Let $V,W$ be finite dimensional vector spaces with $dim(V) = n$ and $dim(W) = k$.
Fix bases $\alpha = \{  v_{1} , \dots, v_{n}\}$ and $\beta = \{  w_{1} , \dots ,w_{2}\}$
With $V - span(\alpha)$, $W = span(\beta)$

Suppose that $T : V\to W$ is a linear transformation with:
$T(v_{i}) = a_{1i}w_{1} + \dots +a_{ki}w_{k} = \sum_{j=1}^{k}a_{ji}w_{j}$
The matrix is represented as:
$$[T]_{\alpha}^{\beta} = \left[\begin{array}{c}
a_{11} \dots a_{1n}  \\ \\
\vdots\\
a_{k1} \dots a_{kn} \\ \\
\end{array}\right]
$$
It starts at basis $\alpha$ and ends in basis $\beta$
# Examples
- [[Finding Matrix Representation for Identity Transformation]]