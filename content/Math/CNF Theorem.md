---
tags:
  - programming
  - math
---
# Theorem
Every [[Propositional Formula]] is logically equivalent to a [[Math/Conjunctive Normal Form|CNF Formula]].
# Example
$F = (X \leftrightarrow Y) \vee (X \to Z)$
1. Start with the truth table, and fill out the $\neg F$ column aswell

| x   | y   | z   | F   | $\neg F$ |
| --- | --- | --- | --- | -------- |
| 0   | 0   | 0   | 1   | 0        |
| 0   | 0   | 1   | 1   | 0        |
| 0   | 1   | 0   | 0   | 1        |
| 0   | 1   | 1   | 0   | 1        |
| 1   | 0   | 0   | 1   | 0        |
| 1   | 0   | 1   | 0   | 1        |
| 1   | 1   | 0   | 1   | 0        |
| 1   | 1   | 1   | 1   | 0        |

2. Arrange the DNF to be the assignments of all those that result in $\neg F = 1$
$$
(\neg x \wedge y \wedge \neg z) \vee
(\neg x \wedge y \wedge z) \vee
(x \wedge \neg y \wedge z) 
$$
3. Then, negate the formula
$$
\neg [(\neg x \wedge y \wedge \neg z) \vee
(\neg x \wedge y \wedge z) \vee
(x \wedge \neg y \wedge z) ]
$$
4. Apply [[Boolean Algebra De-Morgans Law]]
$$
\neg (\neg x \wedge y \wedge \neg z) \wedge
\neg (\neg x \wedge y \wedge z) \wedge
\neg (x \wedge \neg y \wedge z) 
$$
5. Apply [[Boolean Algebra De-Morgans Law]] again
$$
(x \vee \neg y \vee  z) \wedge
(x \vee \neg y \vee \neg z) \wedge
(\neg x \vee y \vee \neg z) 
$$
