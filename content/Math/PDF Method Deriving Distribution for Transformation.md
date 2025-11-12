---
tags:
  - math
  - statistics
---
# Method
- Assume $Y = h(X)$ for [[Continuity|Continuous]] [[Injective Functions|Injective]] function $h$
- Assume [[Probability Density Function|PDF]] $f_{X}(x)$ is known, but there is no closed-form [[Cumulative Distribution Function|CDF]]
- [[Portable Document Format|PDF]] of $Y$ given by:
$$f_{Y}(y) = \frac{f_{X}(h^{-1}(y))}{|h'(h^{-1}(y))|}$$
![[PDF Method Deriving Distribution for Transformation-20251021134123893.webp]]