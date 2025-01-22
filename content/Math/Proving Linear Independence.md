---
tags:
  - math
  - proofs
  - linalg
---
# Strategy
1. Assume linear dependence for contradiction
2. Derive a contradiction
# Example
1. Consider the [[Standard Basis]] at $n=3$. That is: $S = \{ (1,0,0), (0,1,0), (0,0,1) \}$
2. Suppose for sake of contradiction that there are non-zero coefficients that allow a sum of 0. $(x)(1,0,0) + (y)(0,1,0) + (z)(0,0,1) = \overrightarrow{0} = (0,0,0)$
3. $\implies (x,0,0) + (0,y,0) + (0,0,z) = (0,0,0)$
4. $\implies (x,y,z) = (0,0,0)$
5. Therefore: $x=y=z=0$
6. This contradicts that a [[Linear Dependence|Linear Dependent]] set has non-zero coefficients for the sum of 0
7. Therefore, there are no [[Non-trivial vectors]] that are dependent