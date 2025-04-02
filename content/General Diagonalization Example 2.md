---
tags:
  - math
  - linalg
---
# Question
Determine whether matrix is diagonizable
$$
\left[\begin{array}{cc}
7 & -4 & 0\\
8 & -5 & 0\\
6 & -6 & 3\\
\end{array}\right]
$$
# Soln
1. We calculate $X(\lambda) = (\lambda-3)^{2}(\lambda+1)$
2. The geometric multiplicity of $Geo(3)$
$$ \left[\begin{array}{ccc|c} 
4 & -4 & 0 & 0\\
0 & -8 & 0 & 0\\
6 & -6 & 0 & 0\\
\end{array}\right]
$$
$Geo(3) = 2$ by defn of [[Rank]]
3. The geometric multiplicity of $Geo(3)$
$$ \left[\begin{array}{ccc|c} 
8 & -4 & 0 & 0\\
8 & -4 & 0 & 0\\
6 & -6 & 4 & 0\\
\end{array}\right]
\xrightarrow{REF}
\left[\begin{array}{cc} 
1 & 0 & -\frac{2}{3} \\
0 & 1 & -\frac{4}{3}\\
0 & 0 & 0\\
\end{array}\right]
$$
4. This, $Geo(-1) = Alg(-1)$
5. This, $Geo(3) = Alg31)$
6. The final matrix $M$ is a. We use [[Diagonalizable]] definition.