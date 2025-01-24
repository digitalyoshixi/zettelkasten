---
tags:
  - math
  - linalg
aliases:
  - Row-Echelon Form
  - REF
---
A [[System Of Equations]] is in echelon form (EF) if the following 3 conditions hold:
1. In each equation either all the coefficients are zero or the first non-zero coefficients is 1. We say that the firs tnon-zero term $1x_{j(i)}$ is the leading term of its row its column is $j_{i}$
2. Each $r \neq i$, the coefficient $a_{rj(i)}$ of $x_{ji}$ is zero (Only non-zero entry in the column)
3. $j(i) < j(i+1)$ whenever rows $i$ and $i+1$ have non-zero entites ("Echelon/staircase pattern")
Note: Condition 2 causes the leading terms to form a staircase from top-left to bottom right
# Examples

# Concepts
- [[Every Linear System Has A Row-Echelon Form Theorem]]
- [[Elimination Algorithm]]
- [[Basic and Free Variables]]