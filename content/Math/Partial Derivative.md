---
tags:
  - math
  - calculus
---
A derivative used as a part of a larger multidimensional derivative.
We only derive one term and treat all others as constants.
# Definition
For $\frac{ \partial f}{\partial x}$ at $(c_{1},c_{2})$
$$\frac{\partial f}{\partial x}(c_{1},c_{2}) = \lim_{ h \to 0 } \frac{f(c_{1}+h, c_{2}) - f(c_{1},c_{2})}{h}$$
# Notations
- $\frac{\partial}{\partial x}f(x,y)$
- $f_{x}$
# Example
Find the derivative $g(x,y) = x^{2}+y^{2}+1$
### Soln
Fix variable $y$ and consider the rate of change over variable $x$
$\implies \frac{\partial f}{ \partial x} = \frac{\partial}{\partial x}(x^{2}+y^{2}+1)= 2x$
Fix variable $x$ and consider the rate of change over variable $y$
$\implies \frac{\partial g}{\partial y} = \frac{\partial }{\partial y}(x^{2}+y^{2}+1)= 2y$
$\implies$ derivative $g'(x,y) = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}) = (2x,2y)$