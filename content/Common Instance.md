---
tags:
  - programming
  - prolog
---
# Definition
A common instance of [[First Order Term|Term]] $A,B$ if there exists [[Substitution|Substitutions]] $S_{1},S_{2}$ s.t $C = S_{1}(A) = S_{2}(B)$
# Example
- $A = \text{parent}(bob, X)$
- $B = \text{parent}(Y, sue)$
- $S_{1} = \{  X/sue \}$
- $S_{2} = \{  Y/ bob \}$
- $S_{1}(A) = S_{2}(B) = \text{parent}(bob,sue) = C$