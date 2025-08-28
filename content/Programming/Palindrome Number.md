---
tags:
  - programming
---
A [[Leetcode]] problem
# Question
https://leetcode.com/problems/palindrome-number
# Soln
```cpp
#include <iostream>
#include "math.h"
#include <vector>
using namespace std;

int countdigit(int x){
  if (x < 10){
    return 1;
  }
  return 1 + countdigit(x /10);
}


bool isPalindrome(int x) {
    int digits = countdigit(x);
    long long newx = x;
    while (x > 0){
        digits--;
        int rem = x % 10;
        long long power = pow(10,digits);
        newx -= rem * power;
        x = x / 10;
    }
    return newx == 0;
}

int main(){
  bool res = isPalindrome(121);
  cout << res << '\n';
}
```