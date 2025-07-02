---
tags:
  - math
  - linalg
---
# Theorem
- With $A$ as a $m \times n$ matrix
- With $b \in \mathbb{R}^{n}$
- Then, $Ax = b$ always have one squared solution $\bar{x}$
1. $\bar{x}$  is a least squares solution of $Ax = b \Longleftrightarrow$ $\bar{x}$ is a solution of $A^{T}A = A^{T}b$
2. $A$ has linearly independent columns $\Longleftrightarrow A^{T}A$ is [[Linear Map Inverse|Invertible]]. It follows from $1$ that $\bar{x} = (A^{T}A)^{-1}A^{T}b$
# Proof
1. With linear map $L_{A} : \mathbb{R}^{n} \to \mathbb{R}^{m}$
2. We find $\bar{y} \in Range(L_{A})$ such that $|| b - \bar{y} || \leq || b - y ||$
3. Now, we find the vector $\bar{x}$ such that $A \bar{x} = \bar{y}$. If we can find such a  $\bar{x}$, then $\bar{x}$ is the solution because we find we can now map directly to the smallest
4. We take the [[Basis]] of the [[Column Space]] $col(A)$, and apply [[Gram-Schmidt Algorithm]] to convert it into [[Orthonormal Set]], so that we can get the [[Best Approximation]].
5. $b - E(b)$ is orthogonal to the column space of $A$, so if $a_{i}$ is a column of $A_{i}$ then, $a_{i}^{T} (b - E(b)) = \langle \alpha_{i} | b - E(b) \rangle = 0$
6. This is true for all columns, so we would get $A^TAx = A^{T}b$
7. If $A^{T}A$ is [[Linear Map Inverse|Invertible]], then we have a soln $\bar{x} = (A^{T}A)A^{-1}^{T}b$