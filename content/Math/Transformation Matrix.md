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
Fix bases $\alpha = \{  v_{1} , \dots, v_{n}\}$ and $\beta = \{  w_{1} , \dots ,w_{k}\}$
With $V = span(\alpha)$, $W = span(\beta)$

Suppose that $T : V\to W$ is a linear transformation with:
$T(v_{i}) = a_{1i}w_{1} + \dots +a_{ki}w_{k} = \sum_{j=1}^{k}a_{ji}w_{j}$
The matrix is represented as:
$$[T]_{\alpha}^{\beta} = \left[\begin{array}{c}
a_{11} \dots a_{1n}  \\ 
\vdots\\
a_{k1} \dots a_{kn} 
\end{array}\right]
$$
It starts at basis $\alpha$ and ends in basis $\beta$
# Proof 
- Let $A= (A_{ij}) \in \mathbb{F}^{m\times n}$ where scalars $A_{ij}$ are obtained by $T_{\alpha j} = \sum_{i=1}^{m}A_{ij}B_{i}, \forall 1 \leq j \leq n$ where $\beta = \{ \alpha_{1},\dots,a_{n} \}$, $\beta'= \{ \beta_{1},\dots,\beta_{m} \}$
- i.e, $$[T_{\alpha i}]_{\beta'} = 
\left[\begin{array}{c}
A_{1j} \\
A_{2j}  \\
\vdots\\
A_{nj} \\
\end{array}\right]
$$
- Now, let $\alpha \in V$, Then $\alpha = c_{1}a_{1} +\dots+c_{n}a_{n}$
- Thus, $T(a) = T\left(  \sum_{n}^{j=1}c_{j}\alpha_{j}  \right) = \sum_{n}^{}$
# Examples
- [[Finding Matrix Representation for Identity Transformation]]