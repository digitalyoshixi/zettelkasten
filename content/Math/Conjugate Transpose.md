---
tags:
  - math
  - linalg
aliases:
  - Hermitian Transpose
---
# Definition
- With $A := (a_{j,k}) \in \mathbb{C}^{n \times n}$
- Then $A^{*} := (\overline{a_{k,j}})$ is the [[Conjugate Transpose]] of $A$
# Computing Process
Ensure that you work with an [[Orthonormal Set|Orthonormal Basis]].
1. [[Complex Conjugate]] all entries
2. [[Matrix Transposition]]
# Example
$$A = \left[\begin{array}{cc}
2 & 1 + i\\
i & 3 - i
\end{array}\right]$$
We find $A^{*}$
$$
A^{*} = \left[\begin{array}{cc} 
2 & -i\\
1-i & 3+i\\
\end{array}\right]
$$
# Theorems
- [[Conjugate Transpose of Itself is the Original Matrix]]