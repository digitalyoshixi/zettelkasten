---
tags:
  - math
  - linalg
aliases:
  - Row-Echelon Form
  - REF
---
A [[System Of Equations]] is in echelon form (EF) if the following 3 conditions hold:
1. All rows of zero are at the bottom
2. The first non-zero entry in a row is 1. This is the leading one
3. Each leading one is to the right of all leading ones above it
Note: Condition 1 causes the leading terms to form a staircase from top-left to bottom right
![[Echelon Form-20250125010633324.webp]]
# Formal Definition
1. In each equation either all the coefficients are zero or the first non-zero coefficients is 1. We say that the firs tnon-zero term $1x_{j(i)}$ is the leading term of its row its column is $j_{i}$
2. Each $r \neq i$, the coefficient $a_{rj(i)}$ of $x_{ji}$ is zero (Only non-zero entry in the column)
3. $j(i) < j(i+1)$ whenever rows $i$ and $i+1$ have non-zero entites ("Echelon/staircase pattern")
# Examples

# Concepts
- [[Every Linear System Has A Row-Echelon Form Theorem]]
- [[Elimination Algorithm]]
- [[Free Variable]]