---
tags:
  - programming
  - competitive_programming
---
A question using [[Top-down Programming|Memoization]]
# Question
https://leetcode.com/problems/climbing-stairs
# Soln
![[Climbing Stairs-20250821035509240.webp]]
```cpp
int countWays(int n) {

    // Base cases: If there are 0 or 1 stairs,
    // there is only one way to reach the top.
    if (n == 0 || n == 1)
        return 1;

    return countWays(n - 1) + countWays(n - 2);
}

```