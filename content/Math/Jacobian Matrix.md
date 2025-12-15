---
tags:
  - math
  - calculus
aliases:
  - Jacobian Determinant
---
Used for functions with multiple inputs and multiple outputs.
It is the [[Matrix]] of all possible partial derivatives of a function $f : \mathbb{F}_{1}^{n} \mapsto \mathbb{F}_{2}^{n}$ given by:
$$
J(x_{1},x_{2},\dots,x_{n}) = 
 \left[\begin{array}{cc} 
\frac{\partial y_{1}}{x_{1}} & \frac{\partial y_{1}}{x_{2}} & \dots & \frac{\partial y_{1}}{x_{n}}\\ \\
\vdots & \vdots & \vdots & \vdots \\
\frac{\partial y_{n}}{x_{1}} & \frac{\partial y_{n}}{x_{2}} & \dots & \frac{\partial y_{n}}{x_{n}}\\
\end{array}\right]
$$
# 2-Variable Jacobian
$$
|J(x,y)| = 
\left|\begin{array}{cc} 
\frac{\partial h_{1}(x,y)}{\partial x} & \frac{\partial h_{1}(x,y)}{\partial y} \\
\frac{\partial h_{2}(x,y)}{\partial x} & \frac{\partial h_{2}(x,y)}{\partial y} \\
\end{array}\right|
= |\frac{\partial h_{1}(x,y)}{\partial x}\frac{\partial h_{2}(x,y)}{\partial y} - \frac{\partial h_{1}(x,y)}{\partial y}\frac{\partial h_{2}(x,y)}{\partial x}|
$$
