---
tags:
  - math
  - cryptography
aliases:
  - Phi
  - Totient
---
$\phi(x) = \sum{n < x; n\ is\ relatively\ prime\ with\ x}$
Euler's totient is the function that returns how many numbers smaller than x, are [[Coprime]] with x.
# Prime Property
If $x$ is prime: 
$$\phi(x)=x-1$$
# Composite Property
If $x=p*q$, where $p$ and $q$ are prime numbers: $$\phi(x) = \phi (p) * \phi(q) = (p-1)(q-1)$$
# Power Property
$$\phi(x^n)=x^n-x^{n-1}$$