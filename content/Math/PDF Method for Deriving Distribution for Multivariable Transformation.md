---
tags:
  - math
  - statistics
---
# Method - For [[Continuous Random Variable|Continuous RV]] $X,Y$
- With [[Joint Probability Density Function|Joint PDF]] $f_{X,Y}(x,y)$ 
- With differentiable [[Injective Functions|Injective]] [[Functions of Random Variables|Transformation]] $(Z,W) = h(X,Y)$
The [[Joint Probability Density Function|Joint PDF]] of $(Z,W)$ is given by:
$$f_{Z,W}(z,w)= \frac{f_{X,Y}(h^{-1}(z,w))}{|J(h^{-1}(z,w))|}$$
- Where $J(x,y)$ is [[Jacobian Matrix]]
# Inverting
$$(X,Y) = h^{-1}(Z,W)$$
![[PDF Method for Deriving Distribution for Multivariable Transformation-20251021135732593.webp]]
# Example
![[PDF Method for Deriving Distribution for Multivariable Transformation-20251218021344484.webp]]