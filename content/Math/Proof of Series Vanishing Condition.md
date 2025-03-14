---
tags:
  - math
  - proofs
  - calculus
---
# Proof
1. Suppose $\sum a_{n}$ converges to $s \in \mathbb{R}$
2. Then, by the definition of convergence, $\lim_{ n \to \infty }S_{n} = s$
3. WTS: $\lim_{ n \to \infty }a_{n} = 0$
4. Then, consider $\lim_{ n \to \infty }a_{n} = \lim_{ n \to \infty }(a_{n} + 0)$
5. $= \lim_{ n \to \infty }(a_{n} + a_{1} + \dots + a_{n-1} - a_{1} - \dots - a_{n-1})$
6. $= \lim_{ n \to \infty } (S_{n} - S_{n-1})$ by [[Series Partial Sum]]
7. $= \lim_{ n \to \infty }(S_{n}) - \lim_{ n \to \infty }(S_{n-1})$ by [[Limit Properties]]
8. $= \lim_{ n \to \infty }(S_{n}) - \lim_{ n \to \infty }(S_{n})$ as $\lim_{ n \to \infty }(n-1) \sim n$
9. $= s - s$
10. $= 0$
11. $\square$