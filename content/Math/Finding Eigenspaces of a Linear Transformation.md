---
tags:
  - math
  - linalg
---
# Example
For $T(x,y,z,w) = (1x, 2y, 2z, 3w)$, find $E_{1}, E_{2}, E_{3}, E_{4}$ [[Eigenspace]] of $T$
### For $E_{1}$
1. We want $E_{1} = \{ v : T(v) = 1 * v \}$
2. $= ker(T - 1 * I)$
3. 
$$\Longleftrightarrow
\left[\begin{array}{cccc|c} 
1 - 1 & 0 & 0  & 0 & 0\\
0& 2-1 & 0  & 0 & 0\\
0& 0 & 2-1  & 0 & 0\\
0 & 0 & 0  & 3-1 & 0\\
\end{array}\right] 
$$
4. 
$$\Longleftrightarrow
\left[\begin{array}{cccc|c} 
0 & 0 & 0  & 0 & 0\\
0& 1 & 0  & 0 & 0\\
0& 0 & 1  & 0 & 0\\
0 & 0 & 0  & 2 & 0\\
\end{array}\right] 
$$
5. Solving gives $E_{1} = \{ (x,0,0,0) : x \in \mathbb{R} \}$
### For $E_{2}$
1. We want $E_{2} = \{ v : T(v) = 2 * v \}$
2. $= ker(T - 2 * I)$
3. 
$$\Longleftrightarrow
\left[\begin{array}{cccc|c} 
1 - 2 & 0 & 0  & 0 & 0\\
0& 2-2 & 0  & 0 & 0\\
0& 0 & 2-2  & 0 & 0\\
0 & 0 & 0  & 3-2 & 0\\
\end{array}\right] 
$$
4. 
$$\Longleftrightarrow
\left[\begin{array}{cccc|c} 
1& 0 & 0  & 0 & 0\\
0& 0 & 0  & 0 & 0\\
0& 0 & 0  & 0 & 0\\
0 & 0 & 0  & 1 & 0\\
\end{array}\right] 
$$
5. $E_{2} = \{ (0,y,z,0) : y,z \in \mathbb{R} \}$
### For $E_{4}$
1. We want $E_{4} = \{ v : T(v) = 4 * v \}$
2. $= ker(T - 4 * I)$
3. 
$$\Longleftrightarrow
\left[\begin{array}{cccc|c} 
1 - 4 & 0 & 0  & 0 & 0\\
0& 2-4 & 0  & 0 & 0\\
0& 0 & 2-4  & 0 & 0\\
0 & 0 & 0  & 3-4 & 0\\
\end{array}\right] 
$$
4. 
$$\Longleftrightarrow
\left[\begin{array}{cccc|c} 
1 & 0 & 0  & 0 & 0\\
0& 1 & 0  & 0 & 0\\
0& 0 & 1  & 0 & 0\\
0 & 0 & 0  & 1 & 0\\
\end{array}\right] 
$$
5. Then $E_{4} = \{ 0 \}$
