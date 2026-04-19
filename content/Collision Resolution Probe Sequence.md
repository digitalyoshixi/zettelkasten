---
tags:
  - programming
aliases:
  - Collision Linear Probing
  - Collision Quadratic Probing
  - Collision Double Probing
---
A method for [[Collision Resolution]].
In case of hash collision, gets a next available position using a probe function. Probe index `i` stored for future retrieval.
![[Collision Resolution Probe Sequence-20260419022227901.webp]]
# Probes
### Linear Probing
$A[(h(k)+i) \mod m], i = 0, 1, 2, \dots$
### Quadratic Probing
$A[(h(k)+i + c_{1}i + c_{2}i^{2})\mod m], i = 0, 1, 2, \dots$
### Double Hashing
$A[(h(k)+i + h'(k))\mod m], i = 0, 1, 2, \dots$ where $h'(k)$ is another [[Hashing|Hash Function]]
# Complexity
- Worst case insert $\Theta(n)$ time
- [[Expected Analysis]] unsuccessful search: $O(\frac{1}{1- \alpha})$ where $\alpha$ is [[Load Factor]]
- [[Expected Analysis]] successful search: $O(\frac{1}{a} \ln \frac{1}{1-a})$