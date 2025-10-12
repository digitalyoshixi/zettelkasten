---
tags:
  - programming
---
A [[Leetcode]] graphs question.
# Problem
https://leetcode.com/problems/number-of-islands/
# Soln
```cpp
#include "leetcodeutils.hpp"
using namespace std;


void clearisland(vector<vector<char>>& grid, int i, int j){
        grid[i][j] = '0';
        if (j >= 1 && grid[i][j-1] == '1') clearisland(grid, i, j-1);
        if (j < grid[i].size()-1 && grid[i][j+1] == '1') clearisland(grid, i, j+1);
        if (i >= 1 && grid[i-1][j] == '1') clearisland(grid, i-1, j);
        if (i < grid.size()-1 && grid[i+1][j] == '1') clearisland(grid, i+1, j);
}

int numIslands(vector<vector<char>>& grid) {
    int islands = 0;
    for (int i = 0; i < grid.size(); i++){
        for (int j = 0; j < grid[i].size(); j++){
            //cerr << grid[i][j];
            if (grid[i][j] == '1'){
                islands++;
                clearisland(grid, i, j);
            }
        }
    }
    return islands;
}

int main(){
  vector<vector<char>> a = {
  {'1','1','1','1','0'},
  {'1','1','0','1','0'},
  {'1','1','0','0','0'},
  {'0','0','0','0','0'}
  };
  cout << numIslands(a);
}
```