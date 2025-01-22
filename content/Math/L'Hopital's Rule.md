---
tags:
  - calculus
---
# Theorem
1. Suppose $f$ and $g$ are differentiable on $a$
2. If $g(x)$ is non-zero at the point $a$
3. If $\lim_{ x \to a }\frac{f(x)}{g(x)}$ is in [[Indeterminate Form]]
4. Then, $\lim_{ x \to a}\frac{f'(x)}{g'(x)} = \lim_{ x \to a }\frac{f(x)}{g(x)}$
This law is iterative, so if you keep getting [[Indeterminate Form]], then you can repeat this law over and over again.
# Proof
- [[L'Hopital Rule Proof]]
- [[L'Hopital Rule Intuition]]
# Indeterminate Form Approaches
### $\frac{0}{0}, \frac{\infty}{\infty}$
Simply apply l'hopital's rule
### $0*\infty$, $\infty*-\infty$
$0*\infty = \frac{0}{\left( \frac{1}{\infty} \right)}$
### $0^0,\infty^0,1^\infty$
$L = \infty^0$
$\ln(L) = 0\ln(\infty)$
$\frac{0}{(\frac{1}{\ln(\infty)})}$
$\frac{0}{0}$