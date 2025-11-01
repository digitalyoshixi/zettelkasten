---
tags:
  - math
  - calculus
---
$$\lim_{ x \to x_{0} }f(x) \text{ along } c(t) =  \lim_{ t\to b}f(c(t)) $$
# Continuous Definition
- Given a [[Path]] $c:[a,b] \to \mathbb{R}^{n}$ is a curve or path.
- If $\lim_{ t \to b }c(t)=x_{0}$ (continuous)
- Then, $\lim_{ x \to x_{0} }f(x)$ along path $c(t)$ is $f(x_{0})$
# Example
Consider limit $\lim_{ (x,y) \to (0,0) } \frac{xy^{2}}{x^{3}+y^{3}}$ along paths $c_{1}(t) = (0,t)$
This will be $f(c_{1}(t)) = f(0,t) = \frac{t^{2} * 0}{t^{3} + 0} = 0$