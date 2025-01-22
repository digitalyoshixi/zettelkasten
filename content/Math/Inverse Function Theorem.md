---
tags:
  - calculus
aliases:
  - IFT
  - Derivative of Inverse Function
---
The [[Derivative]] of an [[Inverse Function]].
$$(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$$
$$(f^{-1})''(x) = \frac{f''(f^{-1}(x))}{(f'(f^{-1}(x)))^3}$$
# Rigorous Theorem
1. Let $f$ be invertible
2. Let $f$ be differentiable
3. Let $f'(x) \neq 0$ for all $x \in I$
Theorem conclusions:
4. Then, $f^{-1}$ is differentiable
5. Then $(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$
### Proving 4 (That $f^{-1}$ is differentiable)
Too hard at the moment
### Proving 5 (That $(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$)
1. Assume $f, f^{-1}$ are inverses of eachother
2. Assume $f$ is differentiable
3. Assume $f^{-1}$ is differentiable (but this should be proven)
4. And $f'(x) \neq 0$ for all $x \in I$
5. Then $f(f^-1(x)) = x$                                 From [[Inverse Function|Inverse Function Cancellation]]
6. Then $f'(f^{-1}(x)) * (f^{-1})(x) = 1$                From 5, [[Derivative|Chain Rule]]
7. Then $f'(x) = \frac{1}{f'(f^{-1}(x))}$                              Since $f'(x) \neq 0$