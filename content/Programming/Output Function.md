---
tags:
  - programming
---
A function $\lambda$ used in [[Transducers]] to map input sets to output sets.
# Recursive Definition
- $\lambda^{*}(s,\epsilon) = \emptyset$
- $\lambda^{*}(s, w \alpha) = \lambda(\delta^{*}(s,w),\alpha)$