---
tags:
  - math
---
# Definition
$\forall n \in \mathbb{N}, a_{n} < a_{n+1}$
- This is proved by [[Induction|PMI]]
# Example
Show $a_{1} = 1, a_{n+1} = \sqrt{ 1+5a_{n} }$ is strictly increasing:
### Soln
- Define $P(n) : a_{n} < a_{n+1}$
- Proving base case: 
	- $P(1) = 1 < \sqrt{ 6 } = \sqrt{ 1 + 5(1) }= \sqrt{ 1+5a_{n} }$
- Proving induction step:
	- Suppose $\forall n \geq 1, P(n)$ 
	- Then, $a_{n} < a_{n+1}$ by defn of $P(n)$
	- Consider $a_{n+2} = \sqrt{ 1 + 5a_{n+1} } = \sqrt{ 1 + 5(\sqrt{ 1 + 5 a_{n})} } > \sqrt{ 1+5a_{n} }$ as $\sqrt{ \cdot }$ is increasing by defn
	- Thus, $a_{n+1} < a_{n+2}$
	- Thus, $P(n) \implies P(n+1)$
- Thus, $\forall n \geq 1, a_{n} < a_{n+1}$