---
tags:
  - math
  - proofs
  - calculus
---
# Question
Use [[Archimedean Property]] property to prove $Q$ is dense in $R$.
# Proof
We want to show that there exists a $m \in Z$ and a $n \in N$ such that $a < \frac{m}{n} < b$

1. Assume $x,y \in R$ and $x < y$
2. Choose $n$ such that $n > \frac{1}{y-x}$ and $n \in N$               
	1. Then $\frac{1}{n} < y-x$
	1. Then $x <   y-\frac{1}{n}$
3. Choose $m$ such that $m-1 \leq nx < m$
	1. Then $(m-1) \leq nx < m$
	2. Then $x < \frac{m}{n}$
4. Consider $m-1 < n(x)$
	1. Then $m < n(x) + 1$
	2. Then $m < n(y - \frac{1}{n}) + 1$
	3. Then $m < ny - 1 + 1$
	4. Then $m < ny$
	5. Then $\frac{m}{n} < y$
5. Thus $x < \frac{m}{n} < y$
6. $\frac{m}{n} \in Q$
$$\square$$