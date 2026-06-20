---
tags:
  - math
aliases:
  - Stuttering Step
---
A [[Propositional Formula|Formula]] that has the same output for the given behavior regardless of how many duplicate behaviors evaluated.
# Example
If behavior $b$ is $s_{1} \to s_{2} \to s_{2} \to s_{2} \to s_{3} \to s_{3} \to s_{4} \to s_{4} \to \dots$
If behavior $\hat{b}$ is $s_{1} \to s_{2} \to s_{3} \to s_{4} \to \dots$
Then a stuttering insensitive formula $F$ allows for $b \models F \equiv \hat{b} \models F$