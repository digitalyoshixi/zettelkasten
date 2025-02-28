---
tags:
  - math
  - linalg
---
The kernel is the set of inputs for $T : V\to W$ that result in $\overrightarrow{0}$ as the output.
1. Convert the [[Matrix Transformation]] into [[Augmented Matrix]] form
2. Reduce to [[Echelon Form|REF]]
3. Find the values 
# Example 2
Compute kernel of the transformation:
- $T_{1} : \mathbb{R}^{3} \to \mathbb{R}^{3}$ projection to x-axis
### Soln
- Example $T_{1}$
- In coordinates it is: $T_{1}(x,y,z) = (0,0,z)$
![[Computing Kernels-20250212145430070.webp]]
# Example 3
- $T_{2} : \mathbb{R}^{2} \to \mathbb{R}^{2}$ rotation to $\theta = \frac{\pi}{2}$
### Soln
- Example $T_{2}$
- $$T(x,y) = 
\left[\begin{array}{cc}
0 & -1 \\
1 & 0 \\
\end{array}\right]
\left[\begin{array}{cc}
x\\
y\\
\end{array}\right]
= [-y,x]
$$
Thus, $ker(T_{2}) = \{ (0,0) \}$