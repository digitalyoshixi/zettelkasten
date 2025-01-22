---
tags:
  - dynamic_programming
aliases:
  - Memoization
---
Using [[Recursion]] algorithms.
Starts at the final case and then gradually achieves the values for the base case.
**memoizing** means to store the result of a function into another function call
# Fibonacci Sequence Top-down approach
```
// Pseudocode example for top-down

memo = hashmap
Function F(integer i):
    if i is 0 or 1: 
        return i
    if i doesn't exist in memo:
        memo[i] = F(i - 1) + F(i - 2)
    return memo[i]
```