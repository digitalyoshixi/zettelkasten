---
tags:
  - programming
  - dynamic_programming
---
A [[Leetcode]] [[Dynamic Programming]] problem
# Question
https://leetcode.com/problems/pascals-triangle/?envType=problem-list-v2&envId=dynamic-programming
# Soln
```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
  if (numRows == 1){
    return {{1}};
  }
  vector<vector<int>> templist = generate(numRows - 1);
  vector<int> newlist = {1};
  for (int i = 0; i < numRows-2; i++){
    int myint = templist.back()[i];
    newlist.push_back(templist.back()[i] + templist.back()[i+1]);
  }
  newlist.push_back(1);
  templist.push_back(newlist);
  return templist;

    }
};
```