---
tags:
  - math
  - programming
---
# Problem
- For some string $x \in \Sigma^{*}$
- There exists $b(x)$ which represents $x$ in reverse
- Let $BW(L)$ be the set of all backwards strings of $L$
- For example, $L = \{ \text{ark}, \text{bone} \}, BL=\{ \text{kra}, \text{enob} \}$
- Prove that if $L$ is regular, then $BW(L)$ is also regular
# Solution
We prove with [[Proof by Structural Induction]]
Define $B(R)$ as 'There exists a $R'$ s.t $BW(L(R'))=\mathcal{L}(R')$'