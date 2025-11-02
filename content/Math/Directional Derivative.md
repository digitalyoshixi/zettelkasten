---
tags:
  - math
  - calculus
---
# Theorem
- Suppose that $f: \mathbb{R}^{n}\to \mathbb{R}$
- We can define a derivative $f$ at $x$ in direction $v$ to be:
- $Df(x)v = \frac{d}{dt}f(x+tv)|_{t=0}=\lim_{ t \to 0 }\frac{f(x+y)-f(x)}{t} = \nabla f \cdot v$
# Directional Derivative with Gradient
$Df(x)v = \nabla f \cdot v$
# Finding Directional Derivative Process
Given:
- A function $f$
- A origin point $x_{0}$
- A direction vector $v$
1. Find $\nabla f$
2. Evaluate $\nabla f(x_{0})$
3. Find the normal vector $\frac{v}{||v||}$
4. Evaluate $\nabla f(x_{0}) \cdot \frac{v}{||v||}$, this is your directional derivative