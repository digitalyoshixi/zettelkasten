---
tags:
  - math
  - statistics
  - probability
aliases:
  - MGF
---
# Definition
The MGF of [[Random Variable|RV]] $X$ is $m(t) = E(e^{tX}) = \int_{-\infty}^{\infty} e^{tx}f_{X}(x)dx$
- [[Well Defined]] when $m(t)$ is finite $\forall t < \epsilon, \epsilon > 0$
# Properties
- Linearity to multiply: $Y = a_{1}X_{1}+\dots+a_{n}X_{n} \implies m_{Y}(t)=m_{X_{1}}(a_{1}t) \times \dots \times m_{X_{n}}(a_{n}t) = \Pi_{i=1}^{n}m_{X_{i}}(a_{i}t)$
- IID $X_{1},X_{2},\dots,X_{n}, Y = X_{1}+\dots+X_{n} \implies m_{Y}(t) = (m_{X}(t))^{n}$
# Calculating Moments
$$E(X^{k}) = m^{k}(0) = \frac{d^{k}}{dt^{k}}m(t)|_{t=0}$$