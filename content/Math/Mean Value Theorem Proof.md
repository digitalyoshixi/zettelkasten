---
tags:
  - math
  - proofs
  - calculus
---
# Proof:
1. Assume $f$ is continuous on $[a,b]$
2. Assume $f$ is differentiable on $(a,b)$
3. Let $g(x) = f(x) - \text{secant line}$
4. So $g(x) = f(x) - [ \frac{f(b) - f(a)}{b-a}(x-a) + f(a) ]$
4. Note $g$ is continuous on $[a,b]$ since $g$ is a difference of polynomials
5. Note $g$ is differentiable on $(a,b)$ as g is difference of polynomials, you can use derivative rules
6. Note $g(a) = f(a) - [ \frac{f(b) - f(a)}{b-a}(a-a) + f(a) ] = 0$
6. Note $g(b) = f(b)-[ \frac{f(b) - f(a)}{b-a}(b-a) + f(a) ] = 0$
7. By [[Rolle's Theorem]], there exists a $c \in (a,b)$ such that $g'(c) = 0$
8. So, we have shown there is a $c \in (a,b)$ where $f'(c) = \frac{f(b) -f(a)}{b-a} - g'(c) = 0$ this means $f'(c) = \frac{f(b) - f(a)}{b-a}$ 
$$\square$$