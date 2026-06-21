---
tags:
  - math
aliases:
  - Least Upper Bound
  - Approximation Theorem
  - Join
---
It is the least [[Upper Bound]].
Assumes the [[Completeness|Completeness Axiom]]
Most of the time it is the [[Max]], but it can also exist if the maximum doesnt like cases $[0,5)$
# Notation
![[Supremum-20241010094254299.webp]]
- $A \vee B$ picks the supremum of the two
- $\wedge_{P}S$ notes that $S$ is infimum of [[Set]] $P$
Or $s = \sup(S)$
# Definition
Let $S \subset R$ and $s \in R$, we say that $s$ is in the [[Supremum]] of $S$ if:
1. $s$ is an upper bound of $S$ ($\forall x \in S, x \leq s$)
2. if $b$ is an upper bound of $S$,  then $s \leq b$
### Alternate Definition (Approximation Theorem)
We can approximate $\sup(s)$ as close as we wish using elements of $S$.
Given any tolerance $\epsilon$, then the max - $\epsilon$ is not an upper bound.
**Theorem:**
Assume $s$ is an upper bound of a non-empty set $S \subset R$, then 
$s = sup(S) \Longleftrightarrow \forall \epsilon > 0, \exists x \in S$  s.t $s - \epsilon < x$.
##### Proof:
Note $S \neq 0$ and is bounded above (since $s$  is an upper bound) so:
- $sup(S)$ exists by [[Least Upper Bound Property]] of [[Completeness|Completeness Axiom]]
($\implies$)
Assume $s = \sup(S)$
Let $\epsilon >0$ be arbitrary.
Let $b = s-\epsilon$
We want to assume for contradiction that b is an upper bound. This means $\forall x \in S$, $s - \epsilon \geq x$.
$b < s$. This contradicts that $s$ is the least upper bound.
Therefore $b$ is an upper bound is a contradiction. 
Thus $\forall x \in S, s - \epsilon < x$
Thus $s = sup(S) \implies \forall \epsilon >0, \exists x \in S, s - \epsilon < b$
($\Longleftarrow$)
Let $\epsilon > 0$ be arbitrary.
Assume $\exists x \in S$ s.t $s - \epsilon < x$
Assume for contradiction that $B$ is an upper bound and $B < s$
Then $B - B < s - B$
Then $0 < s - B$
Choose $\epsilon = s - B$
Then $s - (s - B) < x$
Then $= B < x$
This means that B is no longer a upper bound. This is a contradiction.
So, our $B < s$ was a contradiction. Thus $B \geq s$
So $s \leq B \implies s = sup(S)$ 
# Concepts
- [[Least Upper Bound Property]]
- [[Proving Supremums]]