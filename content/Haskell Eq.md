---
tags:
  - haskell
---
A [[Haskell Typeclass]] that can be used to check for equivalence or non-equivalence of types.
# Automatic Defining Eq
If you dont define the equals method, [[Haskell]] will create the Eq method:
- The type is only equal to itself
- Will check types recursively, if the pairwise equalities are equal then its equal