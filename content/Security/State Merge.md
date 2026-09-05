---
tags:
  - verification
  - compilers
aliases:
  - Misclassified Merge
---
Two [[State]] $A,B$ can be merged if they are [[State Equivalence|Equal]]

They can be represented by a new common state 
# Example
- State $A$
- State $B$
- Merged state  $C = Or(A,B)$
- All transitions are merged into the new state
# Misclassified Merge
- A negative string is misclassified if it ends in a [[Accepting State]]
- A positive string is misclassified if it ends in a [[Rejecting State]]
# Statistically Acceptable Merge
A merge is acceptable if the proportion of misclassified strings in the DFA is not higher than the proportion of misclassified strings computed before merging.
We test the [[Null Hypothesis]] $H_{0} : p_{1} = p_{2}$ vs the [[Alternative Hypothesis]] $H_{a} : p_{2} > p_{1}$
