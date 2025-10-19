---
tags:
  - math
  - programming
---
With $M, M'$ as [[Deterministic Finite Automaton|DFSA]]
We want $M_{\cdot}$, s.t $\mathcal{L}(M_{\cdot}) = \mathcal{L}(M) \mathcal{L}(M')$
# Intuition
All the exit states in $M$, will then have a transition to the initial state of $M'$
![[FSA Concatenation-20251015135053267.webp]]