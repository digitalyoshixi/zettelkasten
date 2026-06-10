---
tags:
  - programming
aliases:
  - CbC
---
An approach to software development with the aim to product programs guaranteed to be correct with respect to their [[Specification]].
- Create specs before writing code
Avoid [[Software Verification]] after code is written (takes a lot of time)
# Process
1. Encode specification into logical formula
2. Use [[Satisfiability Modulo Theories Solver|SMT Solver]] or [[Synthesis Algorithm]] (Often enhanced by [[Heuristic]]) + [[Oracle]]