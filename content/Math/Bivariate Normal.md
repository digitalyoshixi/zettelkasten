---
tags:
  - math
  - calculus
  - probability
  - statistics
---
We say $X,Y$ follow 2D Normal $$
\left[\begin{array}{cc} 
X\\ 
Y
\end{array}\right] \sim \mathcal{N}(\mu = 
\left[\begin{array}{cc} 
\mu_{X}\\
\mu_{Y}\\
\end{array}\right], \Sigma = \left[\begin{array}{cc} 
\sigma_{X}^{2} & \sigma_{X,Y}\\ 
\sigma_{Y,X} & \sigma_{Y}^{2}
\end{array}\right]
)
$$
if they have a bivariate normal joint pdf
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
![[Bivariate Normal-20251007135544556.webp|678]]
# Properties
- Marginal distributions of multivariate normal are normal
- Linear transformations of normal RVs are normal
- Conditional distributions of multivariate normal are normal