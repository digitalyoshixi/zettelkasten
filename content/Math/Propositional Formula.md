---
tags:
  - math
  - programming
aliases:
  - Formula
---
A set $\mathcal{F}$ of items in [[Propositional Variable|PV]] with propositional closure properties
# Definition
Let $\mathcal{F}$ be the smallest set s.t
### Basis
For every $x \in PV, x \in \mathcal{F}$
### Ind Step
If $p_{1},p_{2} \in \mathcal{F}$
Then, $\neg p_{1}, (p_{1} \wedge p_{2}), (p_{1} \vee p_{2}), (p_{1} \implies p_{2}), (p_{1} \Longleftrightarrow p_{2}) \in \mathcal{F}$