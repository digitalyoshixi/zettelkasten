---
tags:
  - math
  - programming
---
# Method
1. Use [[Proof by Structural Induction]] to define a set $\mathcal{H}$ of formulas that [[Complete Set of Boolean Connectives|uoc]] $C$
2. Define a [[Logical Predicate|Predicate]] $P(F)$ that holds for every $F \in \mathcal{H}$, but not in general
3. Use [[Proof by Structural Induction]] to prove $P(F)$ holds for every formula $F \in \mathcal{H}$
4. Give a specific formula $F$ and show $P(F)$ does not hold, then we show $C$ is not complete
# Intuition
Create a property that [[Complete Set of Boolean Connectives|uoc]] $C$ has, but one that not all formulas have, then show that a formula does not satisfy the property, thereby showing incompleteness.
# Example
Show that set of [[Multiplicative Identity]] and [[Conditional Statement|Implies]] $\{ 1, \to \}$ is not complete 