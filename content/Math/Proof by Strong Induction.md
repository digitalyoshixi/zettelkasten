---
tags:
  - math
  - proofs
aliases:
  - Strong Induction
  - Principle of Complete Induction
  - PCI
---
Used for proving sequences and series.
WTS: $\forall k \geq b, (\forall b \leq i < k,P(i)) \implies P(k)$
1. Suppose arbitrary $k$
2. Suppose $k \geq$ smallest base case
3. Suppose base case 1:
	1. ...
	2. P(1)
4. Suppose base case 2:
	1. ...
	2. P(2)
5. Suppose $k \geq b$
	1. Suppose $\forall b<i<k,P(i)$
	2. ...
	3. $P(k)$
# Proof Strategy
You need to prove manually $P(b), P(b+1), \dots$ (depends on what you need to use)
