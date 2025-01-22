---
tags:
  - math
  - proofs
---
A rational number + an irrational number results in an irrational number 
$$\forall a \in Q, b \not\in Q, a+b \not\in Q$$
# [[Proof By Contradiction]]
Let $a \in Q, b \not\in Q$ be arbitrary.
Assume $a+b \in Q$
It follows that $a+b = \frac{p}{q}$ where $p,q \in Z$ and $q \neq 0$ (by definition of [[Rational Number]])
Furthermore it can be said that, $a = \frac{p_{1}}{q_{1}}$ where $p_{1},q_{1} \in Z$ and $q_{1} \neq 0$ (by definition of [[Rational Number]])
$$(a + b) - a = \frac{p}{q} - \frac{p_{1}}{q_{1}}$$
$$b = \frac{pq_{1} - p_{1}q}{qq_{1}}$$
Note that $pq_{1} - p_{1}q \in Z$ and $qq_{1} \in Z$ (by laws of [[Integer]])
This means that $b \in Q$ (by definition of [[Rational Number]])
This contradicts our statement $b \not\in Q$
Therefore our assumption $a+b \in Q$ is false.
Hence, $a+b \not\in Q$
$\square$