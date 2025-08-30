---
tags:
  - programming
---
A [[Leetcode]] problem with lists.
# Boilerplate
```cpp
#include <iostream>
#include "math.h"
#include <bits/stdc++.h>
#include <vector>
#include <list>
#include <set>
using namespace std;

  bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int i = 0; i < nums.size(); i++){
            int target = nums[i];
            if (seen.contains(target)){
                return true;
            }
            else{
                seen.insert(target);
            }
        }
        return false;
    }

int main(){
  vector<int> myvec = {0, 1, 2, 3, 4, 5, 5};
  cout << containsDuplicate(myvec);
}
```