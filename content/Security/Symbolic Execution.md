---
tags:
  - reverse_engineering
aliases:
  - Static Symbolic Execution
  - Dynamic Symbolic Execution
  - symbex
---
A method of [[Static Analysis]] where we execute symbolic values rather than actual values.
![[Symbolic Execution-20260621204235656.webp|413]]
- We can create a system of constrained branches, and apply it to our input to explore interesting execution paths.

It is approaching a program by viewing it as a set of branching paths, rather than analyzing it input by input.
- For [[Software Verification|Formal Verification]], this is very slow ([[Path Explosion]])
# Process
https://www.youtube.com/watch?v=yRVZPvHYHzw
![[Symbolic Execution-20240629165834957.webp]]
1. Treat the inputs as [[Symbolic Value]]
2. When we encounter a conditional that affects the symbol, we use it to create a constraint and apply it to our symbol
3. The split the path into 2, for both possible paths of execution
Once, we find a branch that leads to a desired execution path, we evaluate the input constraints that lead us there.
Sometimes the input that lead us to a path may have many values, or may be unsatisfiable. If a challenge is written correctly, we should have only 1 input.
# Tools
- [[angr]]
- [[z3]]
- [[cvc5]]
# Concepts
- [[Path Explosion]]
- [[Concolic Analysis]]
# Resources
- https://de-engineer.github.io/SMT-Solvers/
- https://cvc5.github.io/tutorials/beginners/