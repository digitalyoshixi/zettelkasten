---
tags:
  - calculus
  - math
aliases:
  - IT
---
# Theorem
- Given $\sum_{n=i}^{\infty}a_{n}$
- If $f(x)$ is positive
- if $f(x)$ is [[Continuity|Continuous]], on $[i, \infty)$
- If $f(x)$ is [[Strictly Decreasing]] on $[i,\infty)$ 
- if $\forall n \in \mathbb{N}, a_{n} = f(n)$
- Then, $\sum_{n=i}^{\infty}a_{n} \text{ converges } \Longleftrightarrow \int_{i}^{\infty}f(x)dx \text{ converges }$
### Flipped Theorem
- Given $\sum_{n=i}^{\infty}a_{n}$
- If $f(x)$ is negative
- if $f(x)$ is [[Continuity|Continuous]], on $[i, \infty)$
- If $f(x)$ is [[Strictly Increasing]] on $[i,\infty)$ 
- if $\forall n \in \mathbb{N}, a_{n} = f(n)$
- Then, $\sum_{n=i}^{\infty}a_{n} \text{ converges } \Longleftrightarrow \int_{i}^{\infty}f(x)dx \text{ converges }$
# Intuition
Both converge or both diverge
# Examples
Note that we only need to prove $f(x)$ is strictly decreasing with derivatives as [[Differentiable Implies Continuity]]
# Proof
1. Suppose $f(x) > 0$ on $[1, \infty)$
2. Suppose $f(x)$  is con on $[1, \infty )$
3. Suppose $f(x)$ is [[Strictly Decreasing]] on $[1, \infty)$
4. Suppose $\forall n \in \mathbb{N}, a_{n} = f(n)$
5. Note that $a_{2}(1) + \dots +a_{n}(1) \leq \int_{1}^{n}f(x)dx$ as it is a [[Right Riemann Sum]], which is smaller for decreasing functions
6. Note that $a_{1}(1) + \dots +a_{n-1}(1) \ge \int_{1}^{n}f(x)dx$ as it is a [[Left Riemann Sum]], which is greater for decreasing functions
### Proving $\Longleftarrow$
7. Suppose $\int_{a}^{\infty}f(x)dx$ converges
8. WTS $\sum_{n=1}^{\infty}a_{n}$ converges.
9. Note that $a_{2}(1) + \dots +a_{n}(1) \leq \int_{1}^{n}f(x)dx$
10. $\implies a_{1} + a_{2}(1) + \dots +a_{n}(1) \leq a_{1} + \int_{1}^{n}f(x)dx$
11. $\implies S_{n} \leq a_{1} + \int_{1}^{n}f(x)dx$ by definition of [[Series Partial Sum]]
12. Note that both sides are $> 0$
13. It also follows that $S_{n} \leq a_{1} + \int_{1}^{n}f(x)dx < a_1 + \int_{1}^{\infty}f(x)dx$
14. We know that $\int_{a}^{\infty}f(x)dx$ converges, thus it is finite. Additionally, $a_{1}$ is a finite value. Thus, we can denote $a_1 + \int_{1}^{\infty}f(x)dx = M \in \mathbb{R}$
15. Thus, $\forall n \in \mathbb{N}, S_{n} \leq M$
16. So, $S_{n}$ is bounded above
17. Now, we show that $S_{n}$ is increasing.
18. Consider $S_{n+1} = S_{n} + a_{n+1}$. Note that $a_{n+1} > 0$ and $S_{n} > 0$ by 1, 4
19. Thus, $S_{n+1} > S_{n} \forall n \in \mathbb{N}$
	1. Then, by [[Bounded Monotone Convergence Theorem|BMCT]], as $S_{n}$ is increasing and bounded above, our series $S_{n}$ converges