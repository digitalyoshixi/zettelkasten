---
tags:
  - math
  - statistics
---
# Method
- For [[Continuity|Continuous]] [[Injective Functions|Injective]] function $h$ on domain $A = (-\infty, y], y \in \mathbb{R}$
- The inverse image $h^{-1}$ can use [[Cumulative Distribution Function|CDF]] of $X$ to find [[Cumulative Distribution Function|CDF]] of $Y$
$$F_{Y}(y) = P(X \leq h^{-1}(y)) = F_{X}(h^{-1}(y))$$
![[CDF Method Deriving Distribution for Transformation-20251021133614817.webp]]
# Strictly Decreasing Function Method
$$F_{Y}(y) = P(Y \geq y) = P(h(x) \leq y) = P(X \geq h^{-1}(y)) = 1 - F_{X}(h^{-1}(y))$$
# Intuition
- You are essentially graphing $x$ and $y$ based off $h(x)$