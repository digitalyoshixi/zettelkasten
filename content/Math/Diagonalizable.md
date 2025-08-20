---
tags:
  - math
  - linalg
aliases:
  - Diagonalization
---
# Definition
A [[Linear Transform|Linear Map]] $T : V \to V$ for a finite dimensional vector space is diagonalizable if its basis for $V$ consists only of eigenvectors of T.
### Diagonalization Definition
To diagonalize a matrix $A$, it must be expressed as a product of matrixes:
$$A = PDP^{-1}$$
- For some [[Linear Map Inverse|Invertable Matrix]] $P$ (The matrix of eigenvectors [[Column Vector|Column Vectors]])
	- This matrix is comprised of the [[Eigenvector|Eigenvectors]] of $A$
- For a [[Diagonal Matrices|Diagonal Matrix]] $D$ (The diagonal matrix of eigenvalues )
	- This matrix is comprised of the [[Eigenvector|Eigenvalues]] of $A$
Then, it follows that:
$$P^{-1}AP = D$$
# Concepts
- [[Diagonal Matrices]]
# Theorems
- [[Characterization of Diagonizability]]
- [[Diagonalize a Matrix Example]]
- [[Nice Case of Diagonalization]]
- [[Sum Characterization of Diagonalizable]]