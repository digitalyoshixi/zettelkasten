---
tags:
  - math
  - linalg
  - physics
---
A common operation between two $\mathbb{R}^{3}$ vectors.
$$u \times v = (u_{2}v_{3} - u_{3}v_{2}, u_{3}v_{1} - u_{1}v_{3}, u_{1}v_{2}-u_{2}v_{1})$$
$$u \times v = ||v || ||w|| \sin \theta$$
# Cross Product as a Matrix
$$a \times b = 
\left[\begin{array}{cc} 
i & j & k\\
a_{1} & a_{2} & a_{3}\\
b_{1} & b_{2} & b_{3}\\
\end{array}\right]
= i \left[\begin{array}{cc}
a_{2} & a_{3}\\
b_{2} & b_{3}\\
\end{array}\right]
- j \left[\begin{array}{cc} 
a_{1} & a_{3} \\ 
b_{1} & b_{3}
\end{array}\right]
+ k \left[\begin{array}{cc}
a_{1} &a_{2}\\
b_{1} &b_{2}
\end{array}\right]
$$
# Properties
- Length of $a \times b$ is an area of the parllelogram spanned by $a$ and $b$
- $|| a \times b || = ||a ||  || b|| \sin \theta$
- $a \times b$ orthogonal to $a$ and $b$
- Linearity : $(au + bv) \times w = a(u \times w) + b(v \times w)$
- [[Alternating|Anticommutivity]] : $(u \times v) = - (v \times u)$
- Dependence detecting : $\{ u,v \}$ dep $\implies u \times v = 0$
- Distributivity under product: $a \times (b + c) = a \times b + a \times c$
- Distributivity under addition: $(a+b) \times c = a \times c + a \times b$