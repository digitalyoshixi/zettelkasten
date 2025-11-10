---
tags:
  - programming
  - math
---
# Example 2
Given a string $e \in \Sigma^{*}$
For example, $e = xyz + xy + x()\div$
we define:
- $vr(e)$ be the number of occurrences of variables in $e$
	- For example, $vr(xyz + xy + x()\div) = 6$
- $op(e)$  be the number of occurrences operators in $e$
	- For example, $op(xyz+xy+x()\div) = 3$
We define $P(e) : vr(e) = op(e)+1$
Prove that $\forall e \in \mathcal{E}, P(e)$
##### Base Case
Consider 3 cases:
1. $e = x$
2. $e = y$
3. $e = z$
Then, notice that for all cases $vr(e) = 1 = 0+1 = op(e)+1$
##### Induction Step
Let $e_{1}, e_{2} \in \mathcal{E}$
Suppose $P(e_{1}), P(e_{2})$ [[Induction Hypothesis]]
Then, given four cases:
- $e_{1} + e_{2}$
	- Note that $vr(e_{1} + e_{2}) = vr(e_{1}) +vr(e_{2})+1 = op(e_{1})+op(e_{2})+2 \implies vr(e_{1}+e_{2})=op(e_{1}+e_{2})+1$
- $e_{1} - e_{2}$
	- Note that $vr(e_{1} - e_{2}) = vr(e_{1}) +vr(e_{2})+1 = op(e_{1})+op(e_{2})+2 \implies vr(e_{1}+e_{2})=op(e_{1}-e_{2})+1$
- $e_{1} \times e_{2}$
	- Note that $vr(e_{1} \times e_{2}) = vr(e_{1}) +vr(e_{2})+1 = op(e_{1})+op(e_{2})+2 \implies vr(e_{1}+e_{2})=op(e_{1}\times e_{2})+1$
- $e_{1} \div e_{2}$
	- Note that $vr(e_{1} \div e_{2}) = vr(e_{1}) +vr(e_{2})+1 = op(e_{1})+op(e_{2})+2 \implies vr(e_{1}+e_{2})=op(e_{1} \div e_{2})+1$
Thus, we get $\forall e \in \mathcal{E}, P(e)$