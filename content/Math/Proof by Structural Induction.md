---
tags:
  - proofs
  - math
---
Proof method used widely in [[Graph Theory]]
Used to prove some [[Logical Predicate]] $P(x)$ holds for all $x$ of some recursively defined structure.
# Structure
1. Define $P(x)$
##### Base Case
1. With $x$ as a recursive structure
	1. Prove $P(x)$
##### Induction Step
1. Suppose $P(x)$ holds for sub-structures used in recursive step of definition
	1. Prove $P$ holds for the recursively constructed structure
# Example
With a well-formed set of expressions comprised of:
- Variables $x,y,z,\dots$
- Operations $+,-, \times, \dots$
Define the [[Alphabet]] for the expressions $\{ x,y,z,+,-,x,\div, (, ) \}$
Let $\mathcal{E}$ be the smallest set.
##### Base Case
Let our base case be $x,y,z \in \mathcal{E}$
##### Induction Step
Assume $e_{1}, e_{2} \in \mathcal{E}$ then, $(e_{1}+e_{2}), (e_{1} - e_{2}), (e_{1} \times e_{2}), (e_{1} \div e_{2}) \in \mathcal{E}$
...
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
#####  Induction Step
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