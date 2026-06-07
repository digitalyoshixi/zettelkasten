---
tags:
  - reverse_engineering
  - math
aliases:
  - SMT Solver
---
SMT solvers are magic.
They are based off [[Boolean Satisfiability Problem Solvers|SAT Solvers]] but instead of only taking boolean expressions, they can take integers, arrays, arithmetic operations, etc.
# Concepts
- [[Concrete Value]]
- [[Symbolic Value]]
- [[Symbolic Execution]]
- [[Guarded Axiom]]
- [[UNSAT Core]]
# Problem with SMT Solvers
- Only feasible for small problems. Complex problems with several inputs will lead to a [[Path Explosion]] where there are too many possible paths for the computer to go down.
