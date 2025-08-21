---
tags:
  - math
  - linalg
---
# Definition
This is a basis that allows [[Changing Coordinates of Endomorphic Maps|Change of Basis]] to convert a matrix into its [[Jordan Form]]
# Finding Jordan Basis
1. Find all [[Eigenvector|Eigenvalue]] of $A$
2. Find a basis for every [[Eigenspace]]
3. For every basis vector $v$ created by the eigenspace basis:
	1. Find one $v$ which solves $Tv = \lambda v + v$ if possible
4. Those $v$ will form the jordan basis