---
tags:
  - calculus
---
Used for adding up the areas of the rectangles [[Signed Area]] of a function from below between two points $[a,b]$.
[[Riemann Partition|Riemann Partitions]] break the function bodies into several rectangles whose areas are added
# Continuity 'Requirement'
Riemann sums can be applied without any setup however, it should be noted that:
- A converging Riemann sum requires $f(x)$ to be [[Continuity|Continuous]]
- if $f(x)$ is [[Discontinuities|Discontinuous]], then a accurate riemann sum is not guaranteed
# Notation
$$\sum_{i=1}^nf(x_{i}^*)\triangle x$$
- n signifies the number of partitions
	- **Conjecture:** The larger the $n$ value, the more accurate the Riemann sum estimation
- **Conjecture:** if $f(x)$ is increasing on $[a,b]$, $L_{n} \leq A \leq R_{n}$
- **Conjecture:** if $f(x)$ is decreasing on $[a,b]$, $R_{n} \leq A \leq L_{n}$
- $\triangle x = \frac{b-a}{n}$
- $x_{i}^{*}$ is the [[Riemann Partition]] for $x_{i}= a +  i\triangle x$ 
	- $x_{i}^{*} = x_{i-1}$ for [[Left Riemann Sum]]
	- $x_{i}^{*} = x_{i}$ for [[Right Riemann Sum]]
	- $x_{i}^{*} = \frac{x_{i-1} - x_{i}}{2}$ for [[Midpoint Riemann Sum]]
# Riemann Sum Types
![[Riemann Sums-20250109195228811.webp]]
- [[Left Riemann Sum]]
- [[Right Riemann Sum]]
- [[Midpoint Riemann Sum]]
### Classifications
- [[Upper Riemann Sum]]
- [[Lower Riemann Sum]]
- [[Trapezoid Riemann Sum]]
# Concepts
- [[Reverse Engineering Riemann Sums]]
