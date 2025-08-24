---
tags:
  - programming
  - dynamic_programming
---
A [[Leetcode]] dynamic programming problem
# Problem
https://leetcode.com/problems/pascals-triangle-ii
# Soln
https://neetcode.io/solutions/pascals-triangle-ii
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> getRow(int rowIndex) {
    vector<int> retRow = {1};
    
    for (int i = 0; i < rowIndex; i++){
      vector<int> nextRow = {0};

      for (int j=0; j < retRow.size(); j++){
        nextRow.push_back(0);
        nextRow[j] += retRow[j];
        nextRow[j+1] += retRow[j];
      }
      retRow = nextRow;
    }
    return retRow;
}

int main(){
  vector<int> res = getRow(3);
  cout << "[";
  for (int i = 0; i < res.size(); i++){
      cout << res[i] << ",";
  }
    cout << "] \n";
}
```