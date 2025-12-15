---
tags:
  - math
  - calculus
---
For a [[Multiple Integral]] with input variables $x,y$ where $x=g(u,v)$, $y = h(u,v)$
$$\int \int f(x,y)dxdy = \int \int f(g(u,v), h(u,b))| \frac{d(x,y)}{d(u,v)}|dudv$$ 
where: $| \frac{d(x,y)}{d(u,v)}|$ is the [[Norm|Absolute Value]] of the determinant of the [[Jacobian Matrix]] 
$$
| \frac{d(x,y)}{d(u,v)}| = | \det \left[\begin{array}{cc}  
\frac{\partial x}{\partial u} & \frac{\partial x}{ \partial u}\\
\frac{\partial y}{\partial u} & \frac{\partial y}{ \partial u}
\end{array}\right] |
$$
- $| \frac{d(x,y)}{d(u,v)}| = r$ in [[Polar Coordinate]]
- $| \frac{d(x,y)}{d(u,v)}| = r$ in [[Cylindrical Coordinate]]
- $| \frac{d(x,y)}{d(u,v)}| = p^{2}\sin \phi$ in [[Spherical Coordinate]]