---
tags:
  - math
  - linalg
aliases: []
---
An alternate way to write [[System Of Equations]] where:
- Coefficients matrix are on the left 
- Expected constant matrix is on the right side
$$
\left[\begin{array}{ccc|c}
a_{11} & a_{12}\dots & a_{1k} & b_{1} \\
a_{21} & a_{22}\dots & a_{2k} & b_{2} \\ \\
\dots\\
a_{n1} & a_{n2}\dots & a_{nk} & b_{n} \\ \\
\end{array}\right]
$$
# Augmented Subroutine Row Operations
### $\lambda R_{j} \to R_{j}$ (Multiplying by non-zero constant)
$$
\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
x_{j1} & x_{j2} & \dots & x_{jn}  & b_{j}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]

\xrightarrow{\lambda R_{j} \to R_{j}}

\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
\lambda x_{j1} & \lambda x_{j2} & \dots & \lambda x_{jn}  & \lambda b_{j}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]
$$

### $\lambda R_{i}+R_{j} \to R_{j}$ (Adding a multiple of another row)
$$
\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
x_{j1} & x_{j2} & \dots & x_{jn}  & b_{j}\\ \\
\vdots\\
x_{i1} & x_{i2} & \dots & x_{in}  & b_{i}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]

\xrightarrow{\lambda R_{i} + R_{j} \to R_{j}}

\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
\lambda x_{i1} + x{ji} & \lambda x_{i2} + x_{j2} & \dots & x_{in}  & b_{i} \lambda b_{j}\\ \\
\vdots\\
x_{i1} & x_{i2} & \dots & x_{in}  & b_{i}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]
$$
### $R_{i} \leftrightarrow R_{j}$ (Swapping rows)
$$
\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
x_{j1} & x_{j2} & \dots & x_{jn}  & b_{j}\\ \\
\vdots\\
x_{i1} & x_{i2} & \dots & x_{in}  & b_{i}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]


\xrightarrow{R_{i} \leftrightarrow  R_{j}}

\left[\begin{array}{cccc|c}
x_{11} & x_{12} & \dots & x_{1n}  & b_{1}\\ \\
\vdots\\
x_{i1} & x_{i2} & \dots & x_{in}  & b_{i}\\ \\
\vdots\\
x_{j1} & x_{j2} & \dots & x_{jn}  & b_{j}\\ \\
\vdots\\
x_{k1} & x_{k2} & \dots & x_{kn}  & b_{k}\\ \\
\end{array}\right]

$$
# Theorems
- [[Row Operations Preserve Solution Sets of Linear Systems Theorem]]
- [[Row Operations Example]]