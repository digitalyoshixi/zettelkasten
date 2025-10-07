---
tags:
  - math
aliases:
  - Turning Points
  - Local Minima
  - Local Maxima
---
### Loose Definition
- If $f''(c)<0$, we have a local maxima
- If $f''(c)>0$, we have a local minima
### Formal Definition
For minima:
$$\exists \delta>0, 0<|x-c|<\delta \implies f(c)\leq f(x)$$
For maxima:
$$\exists \delta>0, 0<|x-c|<\delta \implies f(c)\geq f(x)$$
### Box Ball Definition
Let $f: U \subset \mathbb{R}^{n} \to \mathbb{R}$ be a function. 
Point $x_{0}$ is a [[Local Extrema|Local Minima]] if:
$\exists$ [[Open Ball|Neighborhood]] $x_{0} \in V \subset U$ s.t $x \in U \implies f(x_{0}) < f(x)$
Point $x_{0}$ is a [[Local Extrema|Local Maxima]] if:
$\exists$ [[Open Ball|Neighborhood]] $x_{0} \in V \subset U$ s.t $x \in U \implies f(x_{0}) > f(x)$

Not to be confused with [[Global Extrema]]
![[Pasted image 20230907201858.png]]
# Local Maxima
**Maximas** are points where the surrounding slopes point downwards.
![[Pasted image 20230907203008.png]]
# Local Minima
**Minimas** are points below their surrounding slopes.
![[Pasted image 20230907202954.png]]
# [[Degree]] from # of turning points
The degree of the graph, will always have at max, (**degree-1**) number of turning points.