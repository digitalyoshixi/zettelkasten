---
tags:
  - proofs
  - programming
  - math
---
Used to prove a language is not regular.
![[Pumping Lemma-20250930005403986.webp|335]]
# Lemma
- Given $L$ as a [[Regular Language]]
- $\forall$ [[String]] $s \in L$, $\exists$ $s'$ comprised of $s$ and a subsequence in $s$ that can be repeated/pumped forever s.t $s' \in L$
# Alternative Lemma
1. If $L$ is a [[Regular Language]]
2. Then, there is an integer $n > 0$ with the property that:
   $(*)$ for any stirng $x \in L$ where $|x| \geq n$, there are strings $u,v,w$ s.t:
	1. $x = uvw$
	2. $v \neq \epsilon$
	3. $|uv| \leq n$
	4. $uv^{k}w \in L, \forall k \in \mathbb{N}$