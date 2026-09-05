---
tags:
  - verification
---
A table $S \cup S \cdot A$ that gathers all [[Membership Oracle|Membership Queries]] done so far.
- Rows $S$ are states
- Columns $S \cdot A$ are states + strings used to distinguish behaviors
- Returns 1 if the word you get by concatenating row and column value is in the language
![[Observation Table-20260629142926183.webp]]
# Extended Rows Observations Table
From the alphabet, you can complete the observation table by adding behaviors to default states.
![[Observation Table-20260629150200207.webp]]
# Properties For Easy [[Finite State Automata|FSA]] Translation
1. $S \cup S \cdot A \to 2^{E}$
2. $\forall t \in S \cdot A, \exists s \in S, row(t) = row(s)$
	1. The extended rows do not bring any new information
3. $\forall s_{1}, s_{2} \text{ s.t } row(s_{1}) = row(s_{2}) \implies \forall a \in A, row(s_{1}a)=row(s_{2}a)$
	1. Two row are the same, it will always be the same