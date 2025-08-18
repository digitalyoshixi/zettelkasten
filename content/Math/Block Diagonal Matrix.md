---
tags:
  - math
  - linalg
---
# Definition
A matrix $A$ is a block diagonal matrix if:
$$A = \left[\begin{array}{cc} 
c_{1}I_{d_{1}} & 0 & \dots & 0\\
0 &c_{2} I_{d_{2}}  & \dots &0\\
0 &\dots &  0 &c_{n}I_{d_{n}} \\
\end{array}\right]$$
Where:
- $I_{d_{j}}$ is the [[Identity Matrix]] of $d_{j} \times d_{j}$
- $c_{j}$ is a [[Eigenvector|Eigenvalue]]
Where $A_{i}$ is a [[Diagonal Matrices|Diagonal Matrix]] with only diagonal values $a$
# Intuition
- This is a [[Diagonal Matrices|Diagonal Matrix]] where eigenvalues can be repeated, and all repeated eigenvalues are right next to eachother