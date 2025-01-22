---
tags:
  - calculus
---
Make a temporary $y$ variable, and perform $\lim_{ n \to \infty }\ln y$ or $\lim_{ n \to \infty }e^y$, then undo the operation.

# Example
1. $\lim_{ x \to \infty }(x-\ln x)$
2. $y = x-\ln x$
3. $\lim_{ x \to \infty }e^y$
4. $= \lim_{ x \to \infty }e^{x-\ln x}$
5. $= \lim_{ x \to \infty } \frac{e^{x}}{e^{\ln x}}$
6. $= \lim_{ x \to \infty } \frac{e^{x}}{x}$
7. $=H= \lim_{ x \to \infty } \frac{e^{x}}{1}$
8. $= \infty$
9. $y = \ln(\infty)$
10. $y = \infty$