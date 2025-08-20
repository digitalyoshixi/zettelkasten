---
tags:
  - math
  - linalg
---
A [[T-Annihilator of a Vector|T-Annihilator]] that is [[Monic Polynomial|Monic]]
# Definition
- Minimal polynomial $p$ for $T$ is the [[Monic Polynomial]]  [[Generator for Ideal]] $M = \{  f \in \mathbb{F}[x] , f(T) = 0\}$
### Alternate Characterizations
- $p$ is the minimal polynomial for $M(T) (M(A))$
- $p$ is the polynomial s.t:
	1. $p$ is [[Monic Polynomial]]
	2. $p(T) = 0$
	3. $p(A) = 0$
	4. if $f(T) = 0$, $f(A) = 0$ $\implies degree(p) \leq degree(f)$
# Intuition
- With $T \in \mathcal{L}(V)$
The minimal polynomial $p$ is the smallest [[Degree]] polynomial such that $p(T) = 0$
# Finding Minimal Polynomial Example
With a matrix 
$$
A = \left[\begin{array}{cc} 
-1 & 0 & 0\\
0 & -1 & 0\\
0 & 0 & 3\\
\end{array}\right]
$$
The minimal polynomial is the [[Characteristic Polynomial]] divided such that it retains $m(A) = 0$
- With characteristic polynomial $f(x) = (x+1)^{2}(x-3)$
- The minimal polynomial $m(x)$ could be:
	- $(x+1)^{2}(x-3)$
	- $(x+1)(x-3)$
- We need to check each polynomial if its equal to 0 or not
	- $(A+I)(A+I)(A-3) = 0$
	- $(A+I)(A-3I) = 0$  *Note that this works, so this is our minimal polynomial*
- The minimal polynomial $m(x) = (x+1)(x-3)$
