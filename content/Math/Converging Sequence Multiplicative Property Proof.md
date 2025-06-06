---
tags:
  - math
  - calculus
  - proofs
---
# Theorem
- If $\{ a_{n} \}$ and $\{ b_{n} \}$ are convergent
- Then, $\{ a_{n}b_{n} \}$ are also convergent
# Proof
1. Suppose $\{ a_{n} \}$ converges to some $a \in \mathbb{R}$
2. Suppose $\{ b_{n} \}$ converges to some $b \in \mathbb{R}$
3. We WTS: $\{ a_{n}b_{n} \}$ converges ($\exists l \in \mathbb{R}, \forall \epsilon > 0, \exists N > 0$ s.t $\forall n \in \mathbb{N}$ if $n > N$ then, $|a_{n} - l | < \epsilon$)
4. Choose $l = ab$
5. Let $\epsilon >0$ be arbitrary
6. Invoke 1,2 with $\epsilon_{1} = \frac{1}{1+|b|}\frac{\epsilon}{2} , \epsilon_{2} = \frac{1}{|a|+1}\frac{\epsilon}{2}, e_{3} = 1$
7. Note that $\exists N_{1} > 0$ s.t $\forall n \in \mathbb{N}, n > N_{1}$ then, $|a_{n} - a| <\epsilon_{1} = \frac{1}{1+|b|}\frac{\epsilon}{2}$ as $\{ a_{n} \}$ converges
8. Note that $\exists N_{2} > 0$ s.t $\forall n \in \mathbb{N}, n > N_{2}$ then, $|b_{n} - b| <\epsilon_{2} = \frac{1}{|a|+1} \frac{\epsilon}{2}$ as $\{ b_{n} \}$ converges
9. Note that $\exists N_{3} > 0$ s.t $\forall n \in \mathbb{N}, n > N_{3}$ then, $|b_{n} - b| < e_{3} = 1$ as $\{ b_{n} \}$ converges)
10. $|b_{n}| - |b| \leq |b_{n} - b|< 1$ by [[Reverse Triangle Inequality]]
11. $\implies |b_{n}| - |b| < 1$
12. $\implies |b_{n}| < 1 + |b|$
13. Choose $N = max \{ N_{1},N_{2}, N_{3} \} > 0$
14. Suppose $n > N$
15. Then, $|a_{n}b_{n} - ab| = |a_{n}b_{n} - ab_{n} + ab_{n} - ab|$
16. $= |b_{n}(a_{n} - a) + a(b_{n} - b)| \leq |b_{n}(a_{n} - a) | + |a(b_{n} - b)|$ by [[Triangle Inequality]]
17. $=|b_{n}||a_{n} - a| + |a| |b_{n} - b|$ by [[Absolute Function for Real Numbers]] properties
18. $= (1+|b|)|a_{n} -a| + |a| |b_{n} - b|$
19. $< (1 + |b|)\frac{1}{1+|b|}\frac{\epsilon}{2} + |a|\frac{1}{|a|+1} \frac{\epsilon}{2} \leq \frac{\epsilon}{2} + (1)\frac{\epsilon}{2} = \epsilon$ as $\frac{1}{|a| +1} \leq 1$
20. $\square$