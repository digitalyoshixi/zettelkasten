---
tags:
  - math
  - proofs
  - calculus
---
# Proving with [[Archimedean Property]]
### Question
Prove that $sup(A) = 2$ where $A=\{1+\frac{1}{n}|n\in N\}$


# Proving with Density
### Process
If we want to prove supremum $sup(S)=\sqrt{ 2 }$
1. Show that $2$ is an [[Upper Bound]] of $S$
2. Show that for all $b$'s that are [[Upper Bound]], then $\sqrt{ 2  } \leq b$
### Proof
1. Prove upper bound
   For all $q \in S$, we have $q^2 < 2$ implying $q < \sqrt{ 2 }$ (since $\sqrt{ * }$) is increasing on $[0,\infty)$
   Thus $\sqrt{  2}$ is an upper bound of $S$
2. Prove least upper bound
   Assume $b \in R$ is an upper bound of $S$
   To derive a contradiction, suppose $b < \sqrt{2 }$
   Since $Q$  is dense in $R$, there exists $q \in Q$ such that $b < q < \sqrt{ 2 }$
   Then $q^2 < 2$, thus $q \in S$. (Hence $b < q$ for some $q \in S$)
   This contradicts $b$ being an upper bound of $S$
   Therefore, it must be that $\sqrt{ 2 } \leq b$
Therefore, $sup(S) = \sqrt{ 2 }$