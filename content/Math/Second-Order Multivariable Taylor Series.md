---
tags:
  - math
  - calculus
---
# Theorem
If $f: U \subset \mathbb{R}^{n} \to \mathbb{R}$ is $C^{3}$ then:
$f(x_{0} + h) = f(x_{0}) + \sum_{i=1}^{n}h_{i} \frac{\partial f}{ \partial x_{i}}(x_{0}) + \frac{1}{2} \sum_{i,j=1}^{n}h_{i}h_{j} \frac{\partial^{2}f}{\partial x_{i} \partial x_{j}}(x_{0}) + R_{2}(x_{0}, h)$
Note that $\lim_{ ||h|| \to 0 } \frac{R_{2}(x_{0},h)}{||h||^{2}} = 0$
The second-order taylor approxmiation is: $f(x_{0} +h) \sim f(x_{0}) + [Df(x_{0})]h + Hf(h)$
# Generalization for Function at Point
$$
f(x) \sim f(a) + Df(a)(x-a) + \frac{1}{2}(x-a)^{T}Hf(a)(x-a)
$$