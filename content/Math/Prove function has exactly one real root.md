---
tags:
  - math
  - calculus
---
Example: Prove $f(x) = 3x^5 + \pi x^3 + 7x - 4$
# Proof:
1. Show there exists a real root
	1. $f(0) = -4$  
	2. $f(1) = \pi+6$  
	2. note that $-4<0<\pi+6$
	3. Then, there exists a $c \in (0,1)$ such that $f(c) = 0$ by [[Intermediate Value Theorem|IVT]]
2. Show that f has at most one real root
	1. Suppose f has two real roots. Assume $f(a) = f(b) = 0$
	2. Note that $f$ is cont on $R$ as $f$ is a polynomial
		1. Thus $f$ is cont on $[a,b]$ as $[a,b] \subset R$
	3. Note that $f$ is diff on $R$ as $f$ is a polynomial
		1. Hence $f$ is diff on $[a,b]$ as $[a,b] \subset R$
	4. Note that $f(a) = f(b)$ by assumption
	5. By [[Rolle's Theorem]], there is a $c \in (a,b)$ such that $f'(c) = 0$
	6. Note that $f'(x) = 15x^4 + 3\pi x^2 + 7 > 0+0+7 > 0$ for all $x \in R$
	7. 5 and 6 are a contradiction
	8. Therefore $f$ has at most one real roots
$$\square$$