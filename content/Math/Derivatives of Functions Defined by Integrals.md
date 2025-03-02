---
tags:
  - math
  - calculus
---
# Principle
# Example
Consider $g(x) = \int_{\sin(x)}^{\cos(x)} \tan^{-1}(t) dt$
Find $g'(x)$
### Soln
1. Note that $f(x) = tan^{-1}(x)$
2. Note that $f(x)$ is [[Continuity|Continuous]] on $\mathbb{R}$
3. This means that $f(x)$ is also [[Continuity|Continuous]] on $[\sin(x), \cos(x)]$
4. Define $F(x) = \int_{c}^{x}f(x)dx$ where $c$ is some constant
5. Then, consider $g'(x) = \frac{d}{dx}(\int_{\sin(x)}^{\cos(x)} f(x) dt)$
6. $= \frac{d}{dx}(\int_{\sin(x)}^{c})f(t)dt + \int_{c}^{\cos(x)}f(t)dt)$ by [[Integral]] union property
7. $= \frac{d}{dx}(- \int_{c}^{\sin(x)})f(t)dt + \int_{c}^{\cos(x)}f(t)dx)$ by [[Integral]] property
8. $= \frac{d}{dx}(F(sin(x)) + F(cos(x)))$ by defn of $F(x)$
9. $= F'(sin(x))cos(x) - F'(cos(x))sin(x)$ by [[Derivative|Chain Rule]]
10. By [[Fundamental Theorem of Calculus Part 2]] $F'(x) = f(x)$
11. Thus, $= f(sin(x))cos(x) - f(cos(x))sin(x)$
12. $= -cos(x)tan^{-1}(sin(x)) - sin(x)tan^{-1}(cos(x))$ by defn of $f(x)$
Done