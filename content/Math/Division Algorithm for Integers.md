---
tags:
  - math
aliases:
  - Euclidean Algorithm for Integers
  - Extended Euclidean Algorithm
---
# Theorem
1. If $f \in \mathbb{Z}$
2. If $d \in \mathbb{Z} \setminus \{  0 \}$
3. Then, there exists a unique $q,r \in \mathbb{Z}$ such that:
	1. $f = dq+r$
	2. Either $r = 0$ or $| r | < |d|$
4. If the remainder $r = 0$, then we say
	1. $d$ divides $f$
	2. $f$ is a multiple of $d$
	3. $q$ is the quotient of $f$ and $d$
# Example
Find the $gcd(20, 15)$
1. $\frac{20}{15} = 15(1) + 5$
2. $\frac{15}{5} = 3(5) + 0$
3. Thus, the $gcd(20,15) = 5$