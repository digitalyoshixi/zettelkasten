---
tags:
  - math
  - programming
---
A unary operation on [[Finite State Automata|FSA]].
Let $M$ be a [[Deterministic Finite Automaton|DFSA]].
Then $M^{*}$ is the [[Finite State Automata|FSA]] where $\mathcal{L}(M^{*}) = \mathcal{L}(M)^{*}$.
# Intuition
![[FSA Kleene Star-20251208154543783.webp]]
The start point is the end state of the original, and all end states loop back to the starting state of $M$