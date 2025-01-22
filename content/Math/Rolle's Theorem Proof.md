---
tags:
  - math
  - proofs
---
Proof:
Assume:
1. Assume $f$ is continuous on $[a,b]$
2. Assume $f$ is differentiable on $(a,b)$
3. $f(a) = f(b)$
4. Suppose $f(a) = f(b) = k$ for some $k \in R$
5. Case (a):
	1. Suppose $f(x)=k$ for all $x \in (a,b)$
	2. Then $f'(x) = 0$ for all $x \in (a,b)$         derivative constant rule
	3. Then $\exists c \in (a,b)$ with $f'(c)=0$          2, ext gen
6. Case (b):
	1. Suppose $\exists x \in (a,b)$ s.t $f(x) >f(a)=f(b)$
	2. Then, by [[Extreme Value Theorem|EVT]], there exists a $c \in(a,b)$ s.t $f(c)$ is a local maxima/minima
		1. Suppose $f(c)$ is a local maxima
			1. Then, note that $f'(c)$ exists as f is differentiable at $c \in(a,b)$
			2. By fermat's theorem, $f'(c)=0$
			3. Thus, $\exists c \in(a,b)$ with $f'(c)=0$
		2. Suppose $f(c)$ is a local minima
			1. Then, note that $f'(c)$ exists as f is differentiable at $c \in(a,b)$
			2. By fermat's theorem, $f'(c)=0$
			3. Thus, $\exists c \in(a,b)$ with $f'(c)=0$
	3. Thus, $\exists c \in(a,b)$ with $f'(c)=0$
7. Thus, $\exists c \in(a,b)$ with $f'(c)=0$