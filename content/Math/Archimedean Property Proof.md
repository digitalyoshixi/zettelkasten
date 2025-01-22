---
tags:
  - math
  - proofs
---
WTS: $na >b \Longleftrightarrow n > \frac{b}{a}$
# Proof
WTS: $n > \frac{b}{a}$
- Note that $\frac{b}{a}$ is a real number
So, we want to show that for any real number, there exists a natural number greater than it

Proof by contradiction:
Assume for contradiction that $\exists x \in R$ such that $\forall n \in N, x \geq n$
Thus $N$ is bounded above.
- Note that $N$ is non-empty
- By the [[Completeness|Completeness Axiom]], $N$ has a supremum
Then there must be a supremum $sup(N) = s$
Consider $s -1$. This is in the set $N$ as it is less than the supremum.
Then, there must be a natural number greater than $s-1$ $\exists m \in N \implies m > s - 1$
This means $m + 1 > s$ through re-arrangement.
as $m \in N \implies m+1 \in N$ and since $m+1 > s$, we have shown that an element in the set $N$ is bigger than the supremum which is a contradiction.
Thus $\exists n \in N, x < n$