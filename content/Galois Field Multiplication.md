---
tags:
  - math
  - cryptography
---
For a galois field of $GF(2^{m})$, we can represent bits as a [[Polynomial]] and perform [[Polynomial Multiplication]] on them, divide by a constant polynomial and get the remainder.
# Example
For bits:
- $000$ can be represented as polynomial $0$
- $001$ can be represented as polynomial $1$
- $010$ can be represented as polynomial $x$
- $011$ can be represented as polynomial $x+1$
- $100$ can be represented as polynomial $x^{2}$
- $101$ can be represented as polynomial $x^{2}+1$
- $110$ can be represented as polynomial $x^{2}+x$
- $111$ can be represented as polynomial $x^{2}+x+1$
For multiplying $100 \times 011$,
- $x^{2} \times (x + 1) = x^{3}+x^{2}$
- This is $1100$