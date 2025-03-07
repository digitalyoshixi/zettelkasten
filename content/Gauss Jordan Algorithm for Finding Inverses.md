---
tags:
  - math
  - linalg
---
Input: A matrix $M \in M_{n \times n}(\mathbb{R})$.
Output: If $M$ has an inverse, output $M^{-1}$
# Algorithm
1. Form an augmented matrix $[M|I]$ with a $n \times n$ identity
2. Reduce $M$ in $[M|I]$ to [[Echelon Form|REF]] and obtain $[A|M']$
3. If $A = I$, then $M' =M^{-1}$, otherwise $M$ is not invertible
# Example
