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
#include <map>
class Solution {
public:

std::map<int, int> mymap;

int climbStairs(int n) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  if (! mymap[n]){
      mymap[n] = climbStairs(n-1) + climbStairs(n-2);  
  }
  return mymap[n];
  
} 
};
```