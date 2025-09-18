---
tags:
  - math
aliases:
  - Differentiable
---
For a point to be differentiable and have a derivative, it must:
1. Be continuous at that point
2. Limit exists at $f'(c)$. That is: $f'(x^-)=f'(x)=f'(x^+)$
# Formal Definition
$f$ is differentiable if at $a$, $f'(x)$ exists.
It is differentiable on an interval $I$ if it is:
- Differentiable at every point in the interior of $I$
- It is right differentiable on closed left endpoints
- It is left differentiable on closed right endpoints
# Alternate Definition
Let $D = Df(x_{0})$
Then, $f$ is differentiable at $x_{0}$ if:
$$\lim_{ x \to x_{0} } \frac{||f(x) - f(x_{0}) - D * (x-x_{0})||}{||x - x_{0}||} = 0$$
# Non Differentiable Cases
1. Cusp. Sharp change from left slope to right slope
![[Derivative-20240214132001847.webp|205]]
2. Vertical Tangent. Sharp change from left/right limits slope to actual slope(which is undefined) 
![[Derivative-20240214132038442.webp|235]]
3. Discontinuity. Not continuous
![[Derivative-20240214132102215.webp|243]]
4. Absolute function point. Sharp change from left limit slope to right limit slope. Consult [[Absolute Function for Real Numbers]]
![[Derivative-20240222201620604.webp|232]]
# Proving Non-Differentiable
Prove that the one-sided derivatives are different.
# Differentiability $\implies$ [[Continuity]]
- [[Differentiable Implies Continuity]]