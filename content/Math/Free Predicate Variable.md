---
tags:
  - programming
  - math
---
The property of a variable to not be bounded by quantifier.
# Definition
A instance of a variable within a formula that has no quantifier or restriction placed on it.
# Example
$\forall x, A(x) \wedge B(x)$
- $x$ in $A(x)$ is bounded
- $x$ in $B(x)$ is free
# Determining Free Variable Via [[Parse Tree of Predicate Formula]]
Can be found by [[Parse Tree of Predicate Formula]].
- Start at the leaf node with that variable
- Continue to move up the tree, if there is no future occurance, then that variable is free
![[Free Predicate Variable-20251121032050704.webp]]
- $x$ in $\forall y ,S(x,y) \to \neg F(y)$