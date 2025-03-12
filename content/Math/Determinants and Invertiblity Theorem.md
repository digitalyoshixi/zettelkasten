---
tags:
  - math
  - linalg
---
# Theorem
A matrix $M \in M_{n \times n}(\mathbb{R})$ is invertible $\Longleftrightarrow$ $\det(M) \neq 0$
# Proof
### Proving $\Longleftarrow$
1. We can prove the contrapositive first
2. Suppose $M$ is not invertible
3. In the [[Echelon Form|REF]] of $M$, we have a row of zeroes
4. Therefore, one of the rows of M is a linear combination of other rows of $M$
5. Thus, the rows of $M$ are dependent, and we get $\det(M) = 0$