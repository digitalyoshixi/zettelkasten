---
tags:
  - math
  - linalg
---
Input: A matrix $M \in M_{n \times n}(\mathbb{R})$.
Output: If $M$ has an inverse, output $M^{-1}$
# Algorithm
1. Form an augmented matrix $[M|I]$ with a $n \times n$ identity
2. Reduce $M$ in $[M|I]$ to [[Echelon Form|REF]] and obtain $[A|M']$
3. If $A = I$, then $M' =M^{-1}$, otherwise $M$ is not invertible
# Proof
1. We start off with $[M|I]$
2. $\xrightarrow{x_{1}} [E_{x_{1}}M|E_{x_{1}}I]$
3. $\xrightarrow{x_{2}} [E_{x_{2}}E_{x_{1}}M|E_{x_{2}}E_{x_{1}}I]$
4. $\dots$
5. $\xrightarrow{x_{k}} [E_{x_{k}}\dots E_{x_{1}}M|E_{x_{k}}\dots E_{x_{1}}I]$
6. Note that the left side of the augmented matrix is $A$ and right right side is $M^{-1}$
7. If we end up getting $A = I$ which means its the identity matrix, then we have successfully found the inverse
8. If we do not get that, then we know immediately that this matrix is not invertible (This may happen if the matrix has redundant rows)
# Example of Successful Invertable
$$
\left[\begin{array}{ccc|ccc}
1 & 2 & 3 & 1 & 0 & 0\\
0 & 4 & 5 & 0 & 1 & 0\\
0 & 0 & 6 & 0 & 0 & 1\\
\end{array}\right]
$$
$\xrightarrow{\frac{1}{6}R_{3}\to R_{3}}$
$$
\left[\begin{array}{ccc|ccc}
1 & 2 & 3 & 1 & 0 & 0\\
0 & 4 & 5 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & \frac{1}{6} \\
\end{array}\right]
$$
$\xrightarrow{\frac{1}{6}R_{3}\to R_{3}}$
$$
\left[\begin{array}{ccc|ccc}
1 & 2 & 3 & 1 & 0 & 0\\
0 & 4 & 5 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & \frac{1}{6} \\
\end{array}\right]
$$
Somewhere down the line, we get:
$\xrightarrow{\dots}$
$$
\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & 1 & -\frac{1}{2} & -\frac{1}{2} + \frac{10}{24}\\
0 & 1 & 0 & 0 & \frac{1}{4} & -\frac{5}{24}\\
0 & 0 & 1 & 0 & 0 & \frac{1}{6} \\
\end{array}\right]
$$
Therefore, the inverse
$$
\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{array}\right] ^{-1}
= 
\left[\begin{array}{ccc}
1 & -\frac{1}{2} & -\frac{1}{2} + \frac{10}{24} \\
0 & \frac{1}{4} & -\frac{5}{24} \\
0 & 0 & \frac{1}{6} \\
\end{array}\right]
$$
