---
tags:
  - math
  - programming
---
Represent a computation as a [[Partial Mapping]] $\sigma \in (X \multimap\to Y)$ where:
- You cannot have conflicting outputs $(x,y) \in \sigma \implies (x,y') \not \in \sigma \wedge y \neq y'$

Represent a collection of computations as $\mathcal{F} \subset (X \multimap\to Y)$ where:
- All finite subsets $\mathcal{G}$ of $\mathcal{F}$, $\exists p \in (X \multimap\to Y)$ s.t $\forall \sigma \in G, \sigma \leq p$ (all items are [[Compatibility|Comparable]] with an item in the original mapping)