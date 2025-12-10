---
tags:
  - proofs
aliases:
  - Loop Invariance
  - LI
---
A statement that is true upon entering the loop, and after every iteration.
Used after loop exit to prove that the algorithm is correct.
A good loop invariant includes:
- All relevant variables required in the final proving statement.
# Proving Loop Invariance
##### Basis
Show that LI holds when entering the loop
##### Induction Step
1. Consider arbitrary iteration of the loop
2. Suppose LI holds before iteration ([[Induction Hypothesis|IH]])
3. WTP LI holds after iteration