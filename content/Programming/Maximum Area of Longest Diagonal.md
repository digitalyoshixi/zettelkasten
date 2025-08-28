---
tags:
  - programming
---
A [[Leetcode]] lists problem
# Question
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
# Soln
```cpp
#include <iostream>
#include "math.h"
#include <vector>
using namespace std;

int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
    int maxfloat = 0;
    int maxarea = 0;
    for (int i = 0; i < dimensions.size(); i++){
        int diag = pow(dimensions[i][0],2) + pow(dimensions[i][1],2);     
        int area = dimensions[i][0] * dimensions[i][1];
        if (diag == maxfloat){
          if (area > maxarea) maxarea = area;
        }
        else if (diag > maxfloat){
            maxfloat = diag;
            maxarea = area;
        }
    }
    return maxarea;
}

int main(){
  vector<vector<int>> myrects = {{6,5},{8,6},{2,10},{8,1},{9,2},{3,5},{3,5}};
  cout << areaOfMaxDiagonal(myrects) << '\n';
}
```