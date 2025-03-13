---
tags:
  - calculus
  - math
aliases:
  - BMCT
---
# Theorem
1. If $\{ a_{n} \}$ is [[Bounded]]
2. If $\{ a_{n} \}$ is [[Monotonic Sequence|Monotone]]
3. In particular, it is either:
	1. [[Strictly Increasing]] and [[Bounded Above]]
	2. [[Strictly Decreasing]] and [[Bounded Below]]
Then, $\{ a_{n} \}$ [[Sequence Convergence|Converges]]
# Proof
### Proving Strictly Increasing and Bounded Above Case
1. Suppose $\{ a_{n} \}$ is [[Bounded Above]]
2. Suppose $\{ a_{n} \}$ is [[Strictly Increasing]]
3. Then, $\exists c \in \mathbb{R}$ s.t $\forall a \in \{ a_{n} \}, a \leq c$
4. Then, $\forall x_{1}, x_{2} \in \mathbb{N}, x_{1} < x_{2} \implies a_{x_{1}}  < a_{x_{2}}$
5. We want to show $\exists l \in R, \forall \epsilon > 0, \exists N > 0$ s.t $n > N \implies |a_{n} - l | < \epsilon$
6. Consider $A = \{ a_{n} | n \in \mathbb{N} \} \subset \mathbb{R}$
7. Note that $a_{1} \in A$ so $A$ is non-empty
8. Note $A$ is bounded above, as we know $\{ a_{n} \}$ is bounded above
9. By the [[Completeness|Completeness Axiom]], the [[Supremum]] of the set $A$ exists
10. Choose $l = sup(A)$
11. Then, choose arbitrary $\epsilon > 0$
12. Choose $N \in \mathbb{N}$ s.t $l - \epsilon < a_{N}$ by definition of supremum
13. Suppose $n > N$
14. Note that $l - \epsilon < a_{N} < a_{n}$ as $\{ a_{n} \}$ is strictly increasing
15. Note by definition that since $l = sup(A), \forall a \in A, a < l$
16. Note $a_{n} \in A$ by definition
17. Then, $a_{n}  \leq l < l + \epsilon$
18. Then, by transitivity of $<$, it follows that $l-\epsilon < a_{n} < l+\epsilon$
19. $\implies -\epsilon < a_{n} -l < \epsilon$
20. $|a_{n} - l | < \epsilon$ by $| \cdot |$ defn
21. Thus, we have shown convergence
22. $\square$
# Examples
- [[Proving Convergence with BMCT]]