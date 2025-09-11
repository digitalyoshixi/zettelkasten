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
- Requires more base cases compared to [[Proof By Induction|PSI]]
- Stronger [[Induction Hypothesis|IH]] compared to [[Proof By Induction|PSI]]
# Structure
WTS: $\forall k \geq b, (\forall b \leq i < k,P(i)) \implies P(k)$
##### Base Cases
Assuming base cases $b, \dots, b+k-1$
1. Let $n = b$
	1. Proof of $P(n)$
2. Let $n = b+1$
	1. Proof of $P(n)$
3. ...
4. Let $n = b + k - 1$
	1. Proof pf $P(n)$
##### Induction Step
1. Let $n \geq b + k$
2. Suppose $P(j)$ holds whenever $b \leq j < n$ [[Induction Hypothesis]]
	1. Proof of $P(n)$
3. Therefore by induction, $P(n)$ holds for all $n > b$ $\square$
