---
tags:
  - dynamic_programming
---
Starts with the base-cases and then gradually works their way up to the nth case.
# Fibonacci Sequence In Bottom-up Approach
```
// Pseudocode example for bottom-up

F = array of length (n + 1)
F[0] = 0
F[1] = 1
for i from 2 to n:
    F[i] = F[i - 1] + F[i - 2]
```

