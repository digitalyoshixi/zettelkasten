---
tags:
  - math
  - calculus
---
# Theorem
- Let $f(x)$, $g(x)$, $h(x)$ be cont on interval $[a,b]$
- If $\forall x \in [a,b], 0 \leq f(x) \leq g(x)$
- If $\int_{a}^{b}g(x)dx$ is cont
- Then, $\int_{a}^{b}f(x)dx$ is cont
# Proof
1. Suppose $\forall x \in [a,\infty] ,0 \leq f(x) \leq g(x)$
2. Suppose $\int_{a}^{\infty}f(x)dx$ [[Sequence Convergence|Converges]]
3. We want to show $\int_{a}^{\infty}f(x)dx$ [[Sequence Convergence|Converges]]
4. Let $A \in [a,\infty)$ be arbitrary
5. $\implies \forall x \in [a,A] \subset [a,\infty), 0 \leq f(x) \leq g(x)$
6. $\implies \int_{a}^{A}0dx \leq \int_{a}^{A}f(x)dx \leq \int_{a}^{A}g(x)dx$ as integrals preserve inequalities
7. $\implies 0 \leq \int_{a}^{A}f(x)dx \leq \int_{a}^{A}g(x)dx$
8. $\implies \lim_{ A \to \infty }0 \leq \lim_{ A \to \infty }\int_{a}^{A}f(x)dx \leq \lim_{ A \to \infty } \int_{a}^{A}g(x)dx$ as limits preserve non-strict inequalities
9. Note that $\lim_{ A \to \infty }\int_{a}^{A}g(x)dx$ converges by (3)
10. Note that $\lim_{ A \to \infty }\int_{a}^{A}f(x)dx$ is the area accumulation function
11. By [[Fundamental Theorem of Calculus Part 2|FToC Part 2]], we know that $\lim_{ A \to \infty }\int_{a}^{A}f(x)dx$ is continuous
12. Thus, $\int_{a}^{\infty}f(x)dx$ converges
