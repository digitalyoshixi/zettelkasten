---
tags:
  - math
  - linalg
---
Recall that [[Linear Transformation Rotation]] is:
$$R_{\theta}(x,y) = (x\cos(\theta) - y\sin(\theta) , y\cos(\theta) + x\sin(\theta))$$
We calculate $R_{e}$ on the standard basis:
$R_{\theta} = (1,0) = (\cos(\theta), \sin(\theta))$
$R_{\theta}(e_{1}) = \cos(\theta) e_{1} + \sin(\theta)e_{2}$
$R_{\theta}(0_{11}) = (-\sin \theta, \cos \theta)$
$R_{\theta}(e_{2}) = (-\sin \theta) e_{1} + \cos(\theta)e_{2}$
This gives:
$$
[R_{\theta}]_{\alpha}^{\alpha} = \left[\begin{array}{cc}
\cos \theta & -\sin \theta  \\
- \sin \theta & \cos \theta \\
\end{array}\right]
$$