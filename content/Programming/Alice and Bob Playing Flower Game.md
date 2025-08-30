---
tags:
  - programming
---
A [[Leetcode]] question
# Question
https://leetcode.com/problems/alice-and-bob-playing-flower-game/
# Soln
```cpp
#include <iostream>
#include "math.h"
#include <vector>
using namespace std;

long long flowerGame(int n, int m) {
  return (long long)n*m/2;
}

int main(){
  long long res = flowerGame(3,2);
  cout << res << '\n';
}
```