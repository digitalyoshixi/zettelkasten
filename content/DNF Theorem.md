---
tags:
  - programming
  - math
---
# Theorem
Every [[Propositional Formula]] is logically equivalent to a [[Disjunctive Normal Form|DNF Formula]]
# Example
$F = (X \leftrightarrow Y) \vee (X \to Z)$
1. Start with the truth table

| x   | y   | z   | F   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 1   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 0   |
| 1   | 0   | 0   | 1   |
| 1   | 0   | 1   | 0   |
| 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 1   |

1. Arrange the DNF to be the assignments of all those that result in 1
$$
(\neg x \wedge \neg y \wedge \neg z) \vee
(\neg x \wedge \neg y \wedge z) \vee
(x \wedge \neg y \wedge \neg z) \vee
(x \wedge y \wedge \neg z) \vee
(x \wedge y \wedge z)
$$$$