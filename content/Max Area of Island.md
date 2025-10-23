---
tags:
  - programming
---
A leetcode [[Depth First Search|DFS]] problem.
# Problem
https://neetcode.io/solutions/max-area-of-island
# Soln
```cpp
int islandSize(vector<vector<int>>& grid, int x, int y){
    std::cout << x << " " << y << '\n';
    if (grid[y][x] == 0) return 0;
    grid[y][x] = 0;
    int retsum = 0;
    if (y +1< grid.size()){
        std::cout << "checking down\n";
        retsum += islandSize(grid, x, y+1);
    }
    if (y-1>= 0){
        std::cout << "checking up\n";
        retsum += islandSize(grid, x, y-1);
    }
    if (x-1>= 0){
        std::cout << "checking left\n";
        retsum += islandSize(grid, x-1, y);
    }
    if (x+1< grid[0].size()){
        std::cout << "checking right\n";
        retsum += islandSize(grid, x+1, y);
    }
    return 1 + retsum;
}

int maxAreaOfIsland(vector<vector<int>>& grid) {
    int maxarea = 0;
    for (int i = 0; i < grid.size(); i++){
        for (int v = 0; v < grid[i].size(); v++){
            if (grid[i][v] == 1){
              int temparea = islandSize(grid, v, i);
              if (maxarea < temparea) maxarea = temparea;
            }
        }
    }
    return maxarea;
}
```