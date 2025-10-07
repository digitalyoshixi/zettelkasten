---
tags:
  - math
  - calculus
  - probability
  - statistics
---
# Joint PDF
$$
f_{X,Y}(x,y)  = \frac{1}{\sqrt{ (2\pi)^{2} 

\left|\begin{array}{cc} 
\sigma_{X}^{2}  & \sigma_{XY}\\
\sigma_{YX}  & \sigma_{Y}^{2}\\
\end{array}\right| }}\exp \{ -\frac{1}{2} 

\left[\begin{array}{cc} 
x - \mu_{X}\\
y - \mu_{Y} 
\end{array}\right]^{T}
\left[\begin{array}{cc} 
\sigma_{X}^{2} & \sigma_{XY}\\
\sigma_{XY} & \sigma_{Y}^{2}\\
\end{array}\right]^{-1}
\left[\begin{array}{cc} 
x - \mu_{X}\\
y - \mu_{Y} 
\end{array}\right]
\}, \forall x,y \in \mathbb{R}^{2}
$$
![[Bivariate Normal-20251007135544556.webp]]