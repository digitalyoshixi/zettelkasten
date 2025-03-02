---
tags:
  - math
  - calculus
---
# Definition
1. Let $a,b \in R, a<b$
2. Suppose $f$ is [[Bounded]] on $[a,b]$ ($\exists c \in R, \forall x \in [a,b], |f(x)| < c$)
3. The lower Darboux sum = $L(f,p) = \sum_{k=1}^{n} m_{i}(x_{i} - x_{i-1})$
	1. Where, $m_{i}$ is $inf\{ f(x) | x \in \{ x_{i-1} \dots x_{i}   \}\}$ [[Infimum]]
4. The upper Darboux sum = $U(f,p) = \sum_{k=1}^{n} M_{i}(x_{i} - x_{i-1})$
	1. Where, $M_{i}$ is $sup\{ f(x) | x \in \{ x_{i-1} \dots x_{i}   \}\}$ [[Supremum]]
# Darboux Sum
### Lower Darboux Sum ($L(f,p)$)
![[Darboux Integral-20250116195902393.webp|471]]
The heights of each rectangle will be the $m_{i}$
### Upper Darboux Sum ($U(f,p)$)
![[Darboux Integral-20250116195949213.webp]]
The heights of each rectangle will be $M_{i}$