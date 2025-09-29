---
tags:
  - math
  - calculus
aliases:
  - Hessian Function
---
# Theorem
With $f : U \subset \mathbb{R}^{n} \to \mathbb{R}$ as $C^{2}$.
The Hessian of $f$ at $x_{0}$ is the function:
$$Hf(x_{0})(h) = \frac{1}{2} \sum_{i,j=1}^{n} \frac{\partial^{2}f}{\partial x_{i} \partial x_{j}}(x_{0})h_{i}h_{j} 
= 
\left[\begin{array}{cc} \\
\frac{\partial^{2}f}{\partial x_{1} \partial x_{1}}(x_{0}) & \dots & \frac{\partial^{2}f}{\partial x_{1} \partial x_{2}}(x_{0})
\end{array}\right]
$$

# 2x2 Example
A $2 \times 2$ matrix of second order [[Partial Derivative]].
$$
H = \left[\begin{array}{cc}
\frac{\partial ^{2} f}{\partial x^{2}} & \frac{\partial ^{2}f}{\partial x \partial y}\\
\frac{\partial ^{2} f}{\partial x \partial y} & \frac{\partial ^{2}f}{\partial y^{2}}\\
\end{array}\right]
$$
