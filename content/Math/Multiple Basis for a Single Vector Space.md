---
tags:
  - math
---
A single vector space can have multiple basis.
# Example
$\{(1,0), (0,1)\}$ and $\{ (1,1) , (1,-1)\}$ are bases of $\mathbb{R}^2$
Proof:
Linear independence: 
Suppose $x(1,1) + y(1,-1) = (0,0)$
$$
\Rightarrow
\left[\begin{array}{cc|c}
1 & 1 & 0\\
1 & -1 & 0
\end{array}\right]
\xrightarrow{(1)(R1 + R2 \to R2)}
\left[\begin{array}{cc|c}
1 & 1 & 0\\
2 & 0 & 0
\end{array}\right]
\xrightarrow{\frac{1}{2}(R2)  \to R2}
\left[\begin{array}{cc|c}
1 & 1 & 0\\
1 & 0 & 0
\end{array}\right]
\xrightarrow{-1(R2) \to R1}
$$
Note that $(1,1)$ and $(1,-1)$ also span $\mathbb{R}^2$