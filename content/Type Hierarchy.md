---
tags:
  - programming
  - math
aliases:
  - Type Stack
---
A solution to [[Girard's Paradox]] where we avoid using the same type by defining:
- `Type 0 : all those types...`
- `Type 1 : N -> Type 0`
- `Type 2 : N -> Type 1`
Implemented with specific [[Calculus of Constructions]] proof assistants.