---
tags:
  - math
  - programming
---
Let $M, M'$ be  [[Deterministic Finite Automaton|DFSA]] where:
- $M = (Q,\Sigma, \delta, s, F)$
- $M' = (Q',\Sigma, \delta', s', F')$
Want $M_{\cap} = (Q_{\cap}, \Sigma, \delta_{\cap}, s_{\cap}, F_{\cap}$ s.t $\mathcal{L}(M_{\cap}) = \mathcal{L}(M) \cap \mathcal{L}(M')$
Where:
- $Q_{\cap} = Q \times Q' = \{ (q,q') | q \in Q, q' \in Q' \}$ ([[State Space Cartesian Product]])
- $\delta_{\cap}( (q,q') , c) = ( \delta(q,c), \delta(q',c))$
- $s_{\cap} = (s, s')$
- $F_{\cap} = F \times F'$
# Properties
- $M_{\cap}$ is a [[Deterministic Finite Automaton|DFSA]]