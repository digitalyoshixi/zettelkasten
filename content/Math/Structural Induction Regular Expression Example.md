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
Define $B(R)$ as 'There exists a $R'$ s.t $BW(L(R'))=\mathcal{L}(R')$
### Base Case
We show that $B(x)$ holds for $\emptyset, \epsilon, a$
1. Let $R = \emptyset, R' = \emptyset$
2. Let $R = \epsilon, R' = \epsilon$
3. Let $R = a, R' = a$
### Induction Step
- Let $S,T \in \mathcal{RE}$
- Suppose $B(S), B(T)$ [[Induction Hypothesis|IH]]
- This means $\exists S', T'$ s.t $\mathcal{L}(S') = BW(\mathcal{L}(S))$ and $\mathcal{L}(T')=BW(\mathcal{L}(T))$
We need to show 3 cases: $B(S+T)$, $B(ST)$, $B(S^{*})$
- Case 1: $R = S+T$
	- Then, $BW(\mathcal{L}(R)) = BW(L(S+T)) = BW(L(S)) \cup BW(L(T))$
	- $= L(S') +L(T')$ by [[Induction Hypothesis|IH]]
	- $=L(S' + T')$ as $+$ order doesnt matter
	- $=L(R')$
- Case 2: $R = ST$
	- Then, $BW(\mathcal{L}(R)) = BW(\mathcal{L}(ST)) = BW(\mathcal{L}(T)) \cdot BW(\mathcal{L}(S))$ as swapping order of concatenation reverses the roder
	- $=\mathcal{L}(T') \cdot \mathcal{L}(S')$ by [[Induction Hypothesis|IH]]
	- $= \mathcal{L}(T'S')$
	- $= \mathcal{L}(R')$
- Case 3: $R = S^{*}$
	- Then, $BW(\mathcal{L}(R)) = BW(\mathcal{L}(R^{*})) = BW(\mathcal{L}(R)^{*})$ as order does not matter for $*$
	- $= L(S')^{*}$
	- $= L(S'^{*})$
	- $=\mathcal{L}(R')$
- Then, by structural induction $B(R)$ holds $\forall R \in \mathcal{RE}$