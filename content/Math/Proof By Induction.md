---
tags:
  - math
  - proofs
aliases:
  - Simple Induction
  - PSI
  - Principle of Simple Induction
---
Proving using patterns.
It is technically a form of [[Proof By Direct Proof]].
1. Write out $P(x)$ represents ...
2. Prove P(1) - the base case. (Do a simple one-line equivalence)
3. Prove $\forall k \geq 1, P(k) \implies P(k+1)$ - induction step
	1. Take arbitrary $k$ and suppose $k \geq 1$
	2. Suppose $P(k)$ - [[Induction Hypothesis]]
	3. Prove $P(k+1)$
# Analogies
## Dominoes
If a domino falls, it will collapse the next one, which will collapse the next one.
The reason why all of them fall is because any domino falling will collapse another one.
# Examples
$P(n)$ : the sum of the first $n$ odd positive integers is $n^{2}$
Prove:
$$\forall  k \geq 1 \implies (P(k) \implies P(k+1))$$
Proving base case:
1. $P(k)$ by definition: $\sum_{i=1}^{k}(2i-1) = k^2$
2. Then $\sum_{i=1}^{1}(2i-1) = 2-1 = 1 = 1^2$
3. Then $P(1)$ by definition of $P(k)$
Proving induction step:
1. Let $k \geq 1$ be arbitrary
2. Assume $P(k)$
3. $P(k)$ by definition: $\sum_{i=i}^{k}(2i-1) = k^2$
4. Then, $\sum_{i=i}^{k+1}(2i-1) = \sum_{i=i}^{k} +2(k+1)-1$
5. Then, $\sum_{i=i}^{k+1}(2i-1) = k^2 +2k+1$
6. Then, $\sum_{i=i}^{k+1}(2i-1) = (k+1)^2$
7. Then, $P(k+1)$ by 6, definition of $P(k)$
8. Then, $P \implies P(k+1)$ by 2, 7 implies
9. Then, $k\geq 1 \implies (P \implies P(k+1)$ by 2, 7 implies
10. Then, $\forall k\geq 1 \implies (P \implies P(k+1)$ by 1, 9 universal gen
$$\square$$
