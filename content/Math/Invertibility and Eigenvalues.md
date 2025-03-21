---
tags:
  - math
  - linalg
---
# Theorem
$A$ is invertible $\Longleftrightarrow$ $\lambda = 0$ is not an [[Eigenvector|Eigenvalue]].
# Proof
### Proving $\implies$
1. Suppose $A$ is invertible
2. Then, $\det(A) = \lambda_{1}\lambda_{2}\dots \lambda_{n} \neq 0$
3. Thus, $\lambda_{1}, \dots,\lambda_{n}$ is not zero
4. Therefore, $\lambda = 0$ is not an eigenvalue of $A$
### Proving  $\Longleftarrow$
1. Suppose $\lambda = 0$ is not an eigenvalue
2. This gives $\lambda_{1},\dots,\lambda_{n} \neq 0$
3. We know $\det(A) = \lambda_{1}\dots \lambda_{n} \neq 0$
4. And so, $A$ is invertible