---
tags:
  - calculus
  - proofs
---
Four step process
1. Let $\epsilon > 0$  be arbitrary
2. Choose $\delta$ =  ?. (note that $\delta > 0$)
3. Assume condition

# Example
Prove $\lim_{ x \to 2}(3x-8)=-2$
WTS: $\forall \epsilon > 0, \exists \delta > 0$ such that $0 < |x-2| , \delta \implies |3x-8-L|<\epsilon$
Let $\epsilon > 0$ be arbitrary
Choose $\delta = \frac{\epsilon}{3}$ (note that $\delta > 0$)
Assume $0 < |x-2| < \delta$
So, $|(3x-8 - -2) = |3x-6|$ (by algebra)
$= |3||x-2|$ (by algebra and properties of absolute value)
by assumption on x, $0 < |x-2| < \delta$ = $3\left( \frac{\epsilon}{3} \right) = \epsilon$
as required to show $\square$
