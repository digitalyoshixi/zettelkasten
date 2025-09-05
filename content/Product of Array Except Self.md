---
tags:
  - programming
---
A leetcode lists question.
# Problem
https://leetcode.com/problems/product-of-array-except-self/
# Soln
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int fullproduct = 1;
        int numc = 0;
        for (int c : nums){
            if (c == 0){
                numc++;
                continue;
            }
            fullproduct *= c;
        }
        vector<int> ret;
        for (int c : nums){
            if (numc >= 2){
                ret.push_back(0);
                continue;
            }
            if (c == 0){
                ret.push_back(fullproduct);
            }
            else{
                if (numc == 1){
                    ret.push_back(0);    
                }
                else{
                    ret.push_back(fullproduct / c);
                }
                
            }
        }
        return ret;
    }
};
```