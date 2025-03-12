---
tags:
  - calculus
---
An integral that is not evaluatable by normal means.
- Not bounded on $[a,b]$ (Type 1)
- If it is bounded, but it has a  [[Asymptote|VA]] (Type 2)
Refer to the solving process for how to solve. Improper integrals can either:
- [[Converging Series|Converge]] to a finite value
- [[Divergent Series|Diverge]] to have infinite area
# Checking if Improper Integral
### Example 1
$\int_{1}^{\infty}\tan^{-1}(x)dx$
- Is not bounded on $[a,b]$ as $[1,\infty)$ cannot be closed
### Example 2
$$\int_{2}^{8}\frac{1}{\sqrt{ x-2 }}dx$$
- Has a V.A at $x=2$
# Solving Improper Integrals
### Example 1 for Type 1
1. $\int_{1}^{\infty}(3x+1)^{-2}dx$
2. $= \lim_{ A \to \infty }\int_{1}^{A}(3x+1)^{-2}dx$
3. By inspection, $\int (3x+1)^{-2}dx = -\frac{1}{3}(3x+1)^{-1}$
4. $=\lim_{ A \to \infty } F(A) - F(1)$
5. $= \lim_{ A \to \infty }-\frac{1}{3}\left( 0-\frac{1}{4} \right) = \frac{1}{12}$
Therefore, the integral converges to $\frac{1}{12}$
### Example 2 for Type 2
1. $\int_{0}^{5}\frac{\ln(x)}{x}dx$
2. Examine where the problematic endpoint is:
	1. If the lower endpoint (0) is problematic, then evaluate $\lim_{ A \to 0^{+} }$
	2. If the upper endpoint $(5)$ is problematic, then evaluate $\lim_{ A \to 5^{-} }$
3. $= \lim_{ A \to 0^{+} } \int_{A}^{5}f(x)dx$
4. By u-sub, choose $u = \ln(x)$
5. Then, $=\lim_{ A \to 0^{+} }\int_{A}^{5} f(x)dx\frac{1}{u}du$
6. $=(\frac{u^{2}}{2}) + C = \frac{(\ln(x))^{2}}{2} + C$
7. Thus, $F(5) - F(A) = \frac{1}{2}(\ln(5)^{2} - \ln(A)^{2})$
8. $= -\infty$, thus the limit does not exist and diverges
### Example 3 for Type 1 and Type 2
1. $\int_{-1}^{1}x^{-2}dx$
2. $= \int_{1}^{0}x^{-2}dx + \int_{0}^{1}x^{-2}dx$
3. $= \lim_{ A \to 0^{-}}\int_{-1}^{A}x^{-2}dx + \lim_{ B \to 0^{+}  }\int_{B}^{1}x^{-2}dx$
4. Note that the second part with $B$ diverges, and that the first part converges, then the entire integral diverges
### Example 3 that requires [[Comparison Theorem]]
1. $\int_{1}^{\infty}\frac{\cos^{5}(3x^{2}+1)+1}{(x^{2}+x^{7}+1)^{2}}dx$
2. Solve with [[Comparison Theorem]]
# Concepts
- [[Comparison Theorem]]
	- [[Comparison Theorem Convergent Case Proof]]