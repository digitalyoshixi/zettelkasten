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
##### 