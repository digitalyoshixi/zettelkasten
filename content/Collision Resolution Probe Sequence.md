---
tags:
  - programming
---
A method for [[Collision Resolution]].
Stores wherever an element is placed during collision for future retrieval defined by a probe.
# Probes
### Linear Probing
$A[(h(k)+i) \mod m], i = 0, 1, 2, \dots$
### Quadratic Probing
$A[(h(k)+i + c_{1}i + c_{2}i^{2})\mod m], i = 0, 1, 2, \dots$
### Double Hashing
$A[(h(k)+i + h'(k))\mod m], i = 0, 1, 2, \dots$ where $h'(k)$ is another [[Hashing|Hash Function]]
# Complexity
- Worst case insert $\Theta(n)$ time