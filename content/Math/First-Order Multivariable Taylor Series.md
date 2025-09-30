---
tags:
  - math
  - calculus
---
# Theorem
- Let $f : U \subset \mathbb{R}^{n} \to \mathbb{R}$ be differentiable at $x_{0}$.
We have the approximations:
$$f(x_{0}+h) =f(x_{0}) + \sum_{i=1}^{n}h_{i} \frac{\partial f}{\partial x_{i}} + R_{1}(x_{0} , h) = f(x_{0}) + [Df(x_{0})]h + R_{1}(x_{0},h)$$
Where $\frac{\lim_{ h \to 0 }R_{1}(x_{0}, h)}{||h||} = 0$
The first order taylor approximation is: 
$$f(x_{0} + h) \sim f(x_{0}) + [Df(x_{0})]h$$
