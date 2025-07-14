---
tags:
  - math
  - linalg
---
# Definition
- With $V$ as a [[Vector Space]]
- Let $\beta = \{  \alpha_{1}, \alpha_{n}\}$ as a [[Ordered Basis]] for $V$
- Suppose $\langle \cdot | \cdot \rangle$ is a [[Standard Inner Product for Vector Spaces|Inner Product]] on $V$
- The matrix of the inner product is $G_{jk} := ( \langle a_{k} | a_{j} \rangle ) \in \mathbb{C} \text{ or } \mathbb{R}$
# Examples
Find the matrix representation of an inner product $\mathbb{R}^{n}$ with a standard basis $\alpha = \{  e_{1},\dots ,e)n \}$
$$
G = \left[\begin{array}{cc} 
\langle e_{1} | e_{1} \rangle & \dots & \langle e_{n} | e_{1} \rangle\\
\vdots\\ \\
\langle e_{1} | e_{n} \rangle & \dots & \langle e_{n} | e_{n} \rangle
\end{array}\right]
$$
$$G = 
\left[\begin{array}{cc} 
1 & 0 \dots & 0\\
0 & 1 \dots & 0\\
\vdots\\
0 & 0 \dots & 1\\
\end{array}\right]$$