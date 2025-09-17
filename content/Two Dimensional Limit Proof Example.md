---
tags:
  - math
  - calculus
---
# Question
Prove that $\lim_{ (x,y) \to (2,1) } (x+5y) = 7$ using [[Limits Formalized Definition|Epsilon Delta Limit Definition]]
# Proof
Intuition is: $\lim_{ x \to (2,1) }(x+5y)=2+5*1 = 7$
Analysis: $\forall \epsilon > 0, \exists \delta > 0 | 0 \leq ||(x,y) - (2,1) ||< \delta \implies |x+5y-7| < \epsilon$
Thus, $|x+5y-7| = |(x-2) + 5(y-1)| \leq |x-2| + 5|y-1|\leq \delta + 5 \delta$