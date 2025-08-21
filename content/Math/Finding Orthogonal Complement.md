---
tags:
  - math
  - linalg
---
# Video
https://invidious.yoshixi.net/watch?v=A5MHWONSqRw

# Example
WIth $U = span \{ (3,-1,0) , (1,0,1)\}$
Find the orthogonal complement $U^{\perp}$
- Then, $U^{\perp} = \{ v \in \mathbb{R}^{3}  | \langle v | u \rangle = 0, \forall u \in U\}$
- Then, $U^{\perp} = \{ v \in \mathbb{R}^{3}  | \langle v | span \{ (3,-1,0) ,(1,0,1) \} \rangle = 0\}$
- Then, $U^{\perp} = \{ v \in \mathbb{R}^{3}  | \langle v | a(3,-1,0) +b (1,0,1) \rangle = 0\}$
- Then, $U^{\perp} = \{ v \in \mathbb{R}^{3}  | a\langle v | (3,-1,0) \rangle +b \langle v | (1,0,1) \rangle = 0\}$
- Then, $U^{\perp} = \{ v \in \mathbb{R}^{3}  | span \{  \langle v | (3,-1,0) \rangle ,\langle v | (1,0,1) \rangle\}  = \{ 0 \}\}$
- Note that the only time the span of two real numbers is 0, is if both numbers is 0
- Then, $U^{\perp} = \{ v \in \mathbb{R}^{3}  | \langle v | (3,-1,0) \rangle = \langle v | (1,0,1) \rangle\ = 0  \}$
- With $v = (x,y,z)$, We get from solving the equations : 
	- $y=3x$
	- $z=-x$