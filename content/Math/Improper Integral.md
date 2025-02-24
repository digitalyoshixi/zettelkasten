---
tags:
  - calculus
---
An integral that is not evaluatable by normal means.
- Not bounded on $[a,b]$
- If it is bounded, but it has a  [[Asymptote|VA]]
You must turn this integral into two separate integrals
# Checking if Improper Integral
### Example 1
$\int_{1}^{\infty}\tan^{-1}(x)dx$
- Is not bounded on $[a,b]$ as $[1,\infty)$ cannot be closed
### Example 2
$$\int_{2}^{8}\frac{1}{\sqrt{ x-2 }}dx$$
- Has a V.A at $x=2$
# Solving Improper Integrals
### Example 1
1. $\int_{1}^{\infty}(3x+1)^{-2}dx$
2. $= \lim_{ A \to \infty }\int_{1}^{A}(3x+1)^{-2}dx$
3. By inspection, $\int (3x+1)^{-2}dx = -\frac{1}{3}(3x+1)^{-1}$
4. $=\lim_{ A \to \infty } F(A) - F(1)$
5. $= \lim_{ A \to \infty }-\frac{1}{3}\left( 0-\frac{1}{4} \right) = \frac{1}{12}$
Therefore, the integral converges to $\frac{1}{12}$