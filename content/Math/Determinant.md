---
tags:
  - math
  - linalg
---
A matrix operation that is useful for determining scale factor that a transformation has on the area of the 'paralellogram' created by a linear transformation on its basis vectors.
![[Determinant-20250314212431689.webp]]
# Definition
The determinant is the alternating [[Multilinear]] function that sends the identity matrix to 1.
### Formal Definition
1. Consider $M_{n \times n}$ as $(\mathbb{R}^{n})^{m}$ where the rows are thought as vectors in $\mathbb{R}^{n}$
2. If $f : M_{n \times n}(\mathbb{R}) \to \mathbb{R}$ is
	1. [[Alternating]]
	2. [[Multilinear]]
	3. Satisfies $f(I) = 1$
	Then, $f = \det$
# Multilinear Properties
### Normalization Property
$\det(I) = 1$
Where $I$ is the [[Identity Transformation]]
### Product Property
$\det(AB) = \det(A)\det(B)$
### Exponential Property
$\det(A^{k}) = (\det(A))^{k}$
### Constant Multiple Property
If $A$ is $n \times n$ matrix
$\det(kA) = k^{n}\det(A)$
### Transpose Property
$\det(A) = \det(A^{T})$ where $A^{T}$ is the matrix transpose of $A$.
### Invertability Property
$\det(A^{-1}) = \frac{1}{\det(A)}$
# Theorems
- [[Determinants and Invertiblity Theorem]]
- [[Determinants and Row Operations]]
- [[Recursive Formula for Determinant]]
# Concepts
- [[Diagonal Matrices]]
- [[Determinant of 1x1 Matrix]]
- [[Determinant of 2x2 Matrix]]