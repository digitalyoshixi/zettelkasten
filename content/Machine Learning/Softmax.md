---
tags:
  - machine_learning
---
A [[Activation Function]].
$$softmax(z)_{i} = \frac{e^{z_{i}}}{\sum_{i=1}^{n}e^{z}_{j}}$$
![[Softmax-20250628010354610.webp]]
Commonly used during output [[Layer|Layers]] of a [[Neural Network|Neural Net]] to normalize all values to $[0,1]$, and ensure all elements in the output add up to 1.
![[Softmax-20251002183115858.webp]]
