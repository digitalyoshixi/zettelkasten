---
tags:
  - programming
  - algorithm
aliases:
  - DFS
---
A [[Bottom-up Programming]] algorithm for [[Path Finding]]. Uses a [[Stack]]
# Algorithm
1. Base case is when `S = D` or `S = NULL`
2. Keep a list of nodes visited
3. If we are not the base case, then visit all [[Neighbourhood|Neighbors]]
# Concepts
- [[DFS Ordering]]
- [[DFS Cycle Detection]]
# Complexity
- Finding node:
	- Avg/Best/Worst: $O(V+E)$ where:
		- $V$ is the number of vertices
		- $E$ is the number of edges
# DFS Program (Length of Path)
```c
#include <stdio.h>
#include <stdlib.h>

int DFS(int adj_mat[5][5], int start_node, int end_node, int* marked){
  if (start_node == end_node){
    return 0;
  }
  marked[start_node] = 1;
  // perform BFS on all neighbours
  for (int i = 0; i < 5; i++){
    if (adj_mat[start_node][i] == 1){
      if (marked[i] == 0){
        return 1 + DFS(adj_mat, i, end_node, marked);
      }
    }
  }
  return 0;
  
}

int main(){
  // create adjacency matrix
  int adj_mat[5][5] = {
                      {0,1,0,1,1},
                      {1,0,1,1,1},
                      {1,1,0,0,0},
                      {1,1,0,0,0},
                      {0,1,0,0,0},
  };
  int adj_mat_2[5][5] = {
                      {0,1,1,1,0},
                      {1,0,0,1,0},
                      {1,0,0,1,0},
                      {1,1,1,0,1},
                      {0,0,0,1,0},
  };

  int marked[5] = {0,0,0,0,0};
  printf("DFS Length: %d\n", DFS(adj_mat_2, 0, 4, marked));

  return 0;
}
```