---
tags:
  - calculus
  - math
---
We want to prove: 
$$\forall c \in \mathbb{R}, \int cf(x) dx = c\int f(x) dx$$
# Proof
1. Let $c \in \mathbb{R}$ be arbitrary
3. Proving $\Leftarrow$
	1. Suppose $c \int f(x)dx$ exists
	2. $=c(F(x)+C)$ by definition of [[Indefinite Integral]]
	3. $= cF(x) + cC$ 
	4. Note that $cC$ is a constant, thus, $\exists cF(x) + C$ which is the antiderivative for $f$
	5. Note that $(cF(x))' = cf(x)$
	6. Thus, by definition of [[Indefinite Integral]], $\int cf(x)dx$ exists