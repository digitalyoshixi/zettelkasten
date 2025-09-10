---
tags:
  - math
  - proofs
---
# Example
Prove that any amount $n \in \mathbb{N}$  can be created from $k, l \in \mathbb{N}$.
# Proof
- Let [[Logical Predicate]] $P (n) : \exists k,l \in \mathbb{N}$ s.t $4k+7l = n$
- Let $b \in \mathbb{N}$
Base Case:
- Let $n=18$
- Then, $k=1,l=2$
- Then, $4k+7l=18=n$
- Thus, $P(18)$
Induction Step:
- Let $n \geq 18$
- Suppose $\exists k, l \in \mathbb{N}$ s.t $4k+7l = n$ ([[Induction Hypothesis]])
- WTP: $\exists k', d' \in \mathbb{N}$ s.t $4k+7l=n+1$
- Case 1: $l > 0$
	- Then choose $k' = k+2, l' = l-1$
	- Note that $4k'+7l' = 4k+7k+1 = n+1$
	- Thus, $P(n+1)$
- Case 2: $l = 0$
	- Then, we know since $$
	- 