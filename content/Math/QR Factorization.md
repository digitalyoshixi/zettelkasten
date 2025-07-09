---
tags:
  - math
  - linalg
---
# Definition
A matrix $A$ that can be represented as a [[Matrix Multiplication]] of $A = QR$ where:
- $Q$ is [[Unitary Operator|Unitary]]
- $R$ is [[Upper Triangular Matrices|Upper Triangular]]
When $A$ is full rank,
- $A = [ a_{1}, \dots, a_{n}]$
- $\{ e_{1},\dots,e_{n} \}$ is the [[Orthonormal Set|Orthonormal Basis]] constructed from [[Gram-Schmidt Algorithm]] of $\{ a_{1},\dots,a_{n} \}$
- $Q = [ e_{1},\dots,e_{n}]$
- $$R = \left[\begin{array}{cccc} 
\langle a_1 | e_{1} \rangle & \dots & & \langle a_{n} | e_{1} \rangle \\ 
0 & \langle a_{2} | e_{2} \rangle & \dots & \langle a_{n} | e_{2} \rangle  \\
\vdots\\
0 & \dots & & \langle a_{n} | e_{n} \rangle
\end{array}\right]$$
