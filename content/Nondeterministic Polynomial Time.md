---
tags:
  - math
aliases:
  - NP
---
A [[Stochastic Algorithm|Stochastic]] algorithm that runs in [[Polynomial Time]].
These are problems that can be verified quickly.
# NP relation
A [[Relation]] $R \subset X \times Y$ is a NP relation if:
- It is [[Polynomial Time]] bounded $|x| \leq p(|y|), \forall (x,y) \in R$
- There exists polynomial time algorithm $V$ s.t $(x,y) \in R \Longleftrightarrow V(x,y) = 1$
