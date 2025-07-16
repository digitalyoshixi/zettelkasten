---
tags:
  - math
aliases:
  - Euclidean Algorithm for Polynomials
---
# Theorem
1. If $f,d \in \mathbb{F}[x]$
2. if $d \neq 0$
3. Then, there exists a unique $q, r \in \mathbb{F}[x]$ s.t:
	1. $f = qd +r$
	2. either $r = 0$ or $deg(r) < deg(f)$
4. If the remainder $r = 0$, then we say:
	1. $d$ divides $f$
	2. $f$ is a multiple of $d$
	3. $q$ is the quotient of $f$ and $d$
You can use the [[Division Algorithm for Polynomials]]
# Process
Given $f_{1}, f_{2}$. [[Without Loss of Generality|WLOG]], let $deg(f_{1}) \geq deg(f_{2})$
1. Set $f = f_{1}, d = f_{2}$, then solve for $q,r$ s.t $f = qd + r$
2. While $r \neq 0$, set $f = d, d = r$, and solve for $q,r$ s.t $f = qd+r$
3. When $r = 0, gcd(a,b) = dxa_{k}^{-1}$ from your last iteration where $a_{k}$ is the leading coefficient of $a$
# Example
Find the $gcd(x^{3} + 2x^{2} - x - 2, x^{2} + 2x +1)$
1. $\frac{x^{3}+ 2x^{2} - x - 2}{x^{2}+2x+1} = (x)(x^{2}+2x+1) + -2x - 2$
2. $\frac{x^{2}+2x+1}{-2x-2} = (-\frac{1}{2}x - \frac{1}{2})(-2x-2) + 0$
3. Thus, $\frac{1}{-2}(-2x-2)$ is the [[Greatest Common Divisor of Polynomials|GCD]]
4. Thus $(x+1)$ is the [[Greatest Common Divisor of Polynomials|GCD]]