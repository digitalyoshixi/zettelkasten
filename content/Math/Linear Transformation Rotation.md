---
tags:
  - linalg
aliases:
  - Linear Map Rotation
  - Rotation Matrix
---
Given a linear map $R_{e} : \mathbb{R}^{2} \to \mathbb{R}^{2}$
We can express $R_{e}(x,y)$ for a given $(x,y)$ vector as:
$$R_{e}(x,y) = (x\cos(\theta) - y\sin(\theta) , y\cos(\theta) + x\sin(\theta))$$
# Intuition
![[Vector Rotation-20250207162758170.webp]]
![[Drawing 2025-02-07 11.26.28.excalidraw]]
Thus, our final formula is:
$$(x\cos(\theta) - y\sin(\theta) , y\cos(\theta) + x\sin(\theta))$$
# Useful Rotations
### $\mathbb{R}^{2}$ y-axis reflection
$$
\left[\begin{array}{cc}
-1 & 0\\
0 & 1\\
\end{array}\right]
$$
### $\mathbb{R}^{2}$ x-axis reflection
$$
\left[\begin{array}{cc}
1 & 0\\
0 & -1\\
\end{array}\right]
$$
### $\mathbb{R}^{2}$ Counter-Clockwise Rotation from Origin
$$
\left[\begin{array}{cc}
\cos \theta & -\sin \theta\\
\sin \theta & \cos \theta
\end{array}\right]
$$
### $\mathbb{R}^{2}$ Reflection about $y=mx$
$$
\frac{1}{1+m^{2}}
\left[\begin{array}{cc}
1 - m^{2} & 2m\\
2m  & m^{2} - 1
\end{array}\right]
$$
##### Reflection of $y=x$
$$
\left[\begin{array}{cc}
0 & 1\\
1 & 0\\
\end{array}\right]
$$
##### Reflection of $y=-x$
$$
\left[\begin{array}{cc}
0 & -1\\
-1 & 0\\
\end{array}\right]
$$