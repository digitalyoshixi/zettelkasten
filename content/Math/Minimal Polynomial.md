---
tags:
  - math
  - linalg
---
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
# Finding the Minimal Polynomial
The minimal polynomial is the [[Characteristic Polynomial]] divided by such that it is of the smallest degree.
- With characteristic polynomial $f(x) = (x+1)^{2}(x-3)$
- The minimal polynomial $p(x) = (x+1)(x-3)$
