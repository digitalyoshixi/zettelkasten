---
tags:
  - proofs
  - programming
---
The goal is to construct a [[Predicate]] $P(n)$ that holds for all input sizes $n$
# Process
1. Define $P(n)$ : If precondition holds, and program runs and, input size is $n$, then the program halts and the postcondition holds after it halts
2. Use [[Proof by Strong Induction|PCI]] to prove that $P(n)$ holds for every $n \in \mathbb{N}$ with base case being the smallest number required of the program