---
tags:
  - math
  - calculus
---
We usually use [[Bounded Monotone Convergence Theorem|BMCT]] on recursively defined functions.
# Example
With the sequence $\{ a_{n} \}$ converges where:
- $a_{1} = \sqrt{ 6 }$
- $a_{n+1} = \sqrt{ 6  + a_{n}}$ if $n \geq 1$
### Proof
##### Proving Bounded Above
1. WTS that $\exists M \in \mathbb{R}$ s.t $\forall n \in \mathbb{N}, a_{n} \leq M$
2. Note that $a_{1} = \sqrt{ 6 } < \sqrt{ 9 } = 3$
3. Similarly, $a_{2} = \sqrt{ 6 +\sqrt{ 6 } } < \sqrt{ 6  + 3} = \sqrt{ 9 } = 3$
4. Similarly, $a_{3} = \sqrt{ 6 + \sqrt{ 6 + \sqrt{ 6 } } } < \sqrt{ 6 +\sqrt{ 6 +3 } } = \sqrt{ 6 + 3 } = \sqrt{ 9 } = 3$
5. So, choose $M = 3$
6. Let $n \in \mathbb{N}$ be arbitrary
7. [[Proof By Induction]]
8. Choose $P(n)$ as $a_{n} < 3$
9. Note that $P(1) = \sqrt{ 6 } < 3$ is true
10. Then, suppose $P(n)$ 
11. Consider $\sqrt{ 6+a_{n} } < \sqrt{ 6+3 } = 3$
12. Then, $P(n+1)$ holds by definition of the sequence
13. Thus, we know that $\forall n \in \mathbb{N}, a_{n} < 3$
14. Thus, $\{ a_{n} \}$ is bounded above
##### Proving Strictly Increasing
1. Let $n \in \mathbb{N}$ be arbitrary
2. Consider $a_{n}^{2} - a_{n+1}^{2}$
3. $= a^{2}_{n} - \sqrt{ 6 - a_{n} }^{2}$
4. $= a^{2}_{n} - 6 - a_{n}$
5. $= (a_{n} - 3)(a_{n} + 2)$
6. Note that the $a_{n} > 0$ by sequence definition
7. Note that $a_{n} < 3$ by 8
8. Thus, $(a_{n} - 3)(a_{n} + 2) < 0$ by parity
9. This means $a_{n}^{2} - a_{n+1}^{2} < 0$
10. $\implies a_{n}^{2} < a_{n+1}^{2}$
11. $\implies a_{n} < a_{n+1}$ as $\sqrt{ \cdot }$ function is increasing, ineq prop
12. Then, we get $\{ a_{n} \}$ is increasing by definition
As we have shown $\{ a_{n} \}$ is bounded above and increasing, then we have shown it converges by [[Bounded Monotone Convergence Theorem|BMCT]]
13. Choose $x_{1},x_{2} \in \mathbb{N}$ arbitrarily where $x_{1} < x_{2}$
14. We do [[Proof By Induction]]
15. With $P(n)$ as $a_{n} < a_{n+1}$
16. Note that $a_{1} = \sqrt{ 6 }$
17. $a_{2} = \sqrt{ 6 + \sqrt{ 6 } }$
