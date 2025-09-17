---
tags:
  - proofs
  - programming
  - math
---
The proofs that show that given a set of conditions to run a program, the program [[Turing Machine Halt|Halts]] and returns a desired result.
$$\text{if precondition then (termination and postcondition)}$$
# Proving
Can be proven by showing:
1. [[Termination]] ($\text{precondition } \implies \text{ termination}$)
2. [[Partial Correctness Step]] ($(\text{precondition and termination}) \implies \text{postcondition}$)
# Techniques