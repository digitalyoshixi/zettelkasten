---
tags:
  - math
  - linalg
---
# Theorem
Given $x \in \mathbb{R}^{n}$:
- $f$ as the  [[Quadratic Form]] $f(x) = \sum_{i=1}^{n}a_{ij}x_{i}x_{j}$
- With $A : a_{ij}$
- Then, $x^{T}Ax= f(x)$
Given $x \in \mathbb{C}^{n}$:
- $f$ as the  [[Quadratic Form]] $f(x) = \sum_{i=1}^{n}a_{ij}\overline x_{i}x_{j}$
- With $A : a_{ij}$
- Then, $x^{*}Ax= f(x)$
 ![[Matrix Representation of Quadratic Form-20250718145746731.webp]]
# For $2 \times 2$ Matrix Example
### For $\mathbb{R}$
1. With $x \in \mathbb{R}^{n}$
2. With $f$ as a quadratic form $f(x) = ax_{1}^{2} + b x_{1}x_{2} + cx_{2}^{2}$
3. $$A = \left[\begin{array}{cc} 
a & \frac{b}{2}\\
\frac{b}{2} & c\\
\end{array}\right]$$
### For $\mathbb{C}$
1. With $x \in \mathbb{R}^{n}$
2. With $f$ as a quadratic form $f(x) = a_{11}|x_{1}|^{2} + a_{12} \overline x_{1}x_{2} + a_{21} \overline x_{2}x_{1} + a_{22}|x_{2}|^{2}$
3. $$A = \left[\begin{array}{cc} 
a_{11} & a _{12}\\
a_{21} & a _{22}
\end{array}\right]$$