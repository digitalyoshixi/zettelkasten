---
tags:
  - security
  - cryptography
---
The property of two functions with the same properties to hold the same properties if given inputs from the other function.

[[Universal Composability]] attempts to create algorithms that will be secure for all keys and inputs.
# Non-Composability Example
This is an example where a function does not have security under composition.
- $Gen(\lambda)$, samples $sk \leftarrow \{ 0,\tau \}^{\lambda}$