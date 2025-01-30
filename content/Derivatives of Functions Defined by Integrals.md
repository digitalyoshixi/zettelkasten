---
tags:
  - math
  - calculus
---
# Example
Consider $g(x) = \int_{\sin(x)}^{\cos(x)} \tan^{-1}(t) dt$
Find $g'(x)$
### Soln
1. Note that $f(x) = tan^{-1}(x)$
2. Note that $f(x)$ is [[Continuity|Continuous]] on $\mathbb{R}$
3. This means that $f(x)$ is also [[Continuity|Continuous]] on $[\sin(x), \cos(x)]$
4. Define $F(x) = \int_{c}^{x}f(x)dt$ where $c$ is some constant
5. Then, consider $g'(x) = \frac{d}{dx}(\int_{\sin(x)}^{\cos(x)} f(x) dt)$
6. $= \frac{d}{dx}(\int_{\sin(x)}^{c})f(t)dt + \int_{c}^{\cos(x)}f(t)dt)$ by [[Integral]] union property
7. $= \frac{d}{dx}$