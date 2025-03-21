---
tags:
  - math
  - linalg
---
# Theorem
If $A$ has [[Eigenvector|Eigenvalues]], $\lambda_{1}, \dots, \lambda_{n}$, then $\det(A) = \Pi^{n}_{i=1} \lambda_{i}$
Refer to [[Product Notation|Pi Notation]]
# Proof
Consider characteristic polynomial $X(\lambda) = \det(A - \lambda I)$
If we input $\lambda = 0$, we get $X(0) = \det(A - 0I) = \det(A)$
Given polynomail is also factor
$X(\lambda) = (\lambda_{1} - \lambda) (\lambda_{2} - \lambda)\dots(\lambda_{n} - \lambda)$
These are eigenvalues of $X(\lambda)$
$X(0) = (\lambda_{1} - 0) (\lambda_{2} - 0)\dots(\lambda_{n} - 0)$
