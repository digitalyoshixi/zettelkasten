---
tags:
  - programming
  - math
aliases:
  - First Order Logic
  - FO
---
Logic that uses [[Predicate]] rather than [[Quantifier]] or [[Relation]]
# Concepts
- [[First Order Language]]
# Example
Let [[Domain]] $D$ be the set of all people
- $M(x) : \text{x is male}$
- $S(x,y) : \text{x and y are siblings}$
$$S(x,y) \wedge (M(x) \Longleftrightarrow \neg M(y))$$ Indicates that $x$ and $y$ are brother and sister