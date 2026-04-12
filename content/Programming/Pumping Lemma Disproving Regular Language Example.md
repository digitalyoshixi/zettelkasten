---
tags:
  - math
  - programming
---
# Example
With $\Sigma = \{ 0, 1 \}$
With $L = \{ x \in \Sigma^{*} : x^{R} = x \}$
Prove $L$ is not regular.
- Suppose [[Proof By Contradiction|For Sake of Contradiction]], that $L$ is [[Regular Language]]
- Let $n$ be as in the [[Pumping Lemma]]
- Let $x = 0^{n} 1 0^{n} \in L$
- Then, $|x| = 2n + 1 \geq n$
- Choose $u = 0^{j}$ for some $j \in 0 < k \leq n$
- By 4, $uv^{2}w = u v v w = 0^{n+j}10^{n} \not \in L$ as its not reversible
- Thus, we have a contradiction.
