---
tags:
  - math
  - proofs
---
https://www.youtube.com/watch?v=meudJkjKEe8&t=0s
# Proof
Assume that $\sqrt{ 2 } \in Q$.
This means that $\sqrt{ 2 } = \frac{a}{b}$ where $a,b \in Z$ and the [[GCF]] is 1.
Squaring both sides $$2 = \frac{a^2}{b^2}$$
Rearranging we get:
$$2b^2=a^2$$
this implies that $a^2$ is an [[Even Integer]].
This further implies that $a$ is an [[Even Integer]] ([[Square Has Same Parity Proof]])
$a=2k$ where $k\in Z$
Then rewrite:
$$2b^2=(2k)^2$$
$$b^2=2k^2$$
This implies that $b^2$ is an [[Even Integer]] and $b$ is an [[Even Integer]] by [[Square Has Same Parity Proof]]
Since $b$ and $a$ are even, they have a shared [[GCF]] of atleast 2.
This contradicts our initial assumption of a [[GCF]] of 1.
Therefore $\sqrt{ 2 } \notin Q$
$\square$