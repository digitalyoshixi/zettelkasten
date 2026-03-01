---
tags:
  - programming
  - algorithm
aliases:
  - BFS
---
A [[Path Finding|Graph Traversal]] algorithm that searches in 'rings'. Uses a [[Queue]]
# Algorithm
### [[Top-down Programming]]
1. Starts at vertex 0
2. Save to-visit nodes in a [[Queue]]
3. Mark first node as visited
4. Add the first neighbour nodes to the queue
5. Go through each node in queue until queue is empty
	1. For all the current node's neighbours unvisited, mark them visited and add them to queue
# Complexity
- Finding Node: 
	- Avg/Best/Worst: $O(V+E)$ where
		- $V$ is the number of vertices
		- $E$ is the number of edges
# C Find Node Example
```c
#include <stdio.h>
#include <stdlib.h>


typedef struct LL_Node_Struct{
  struct LL_Node_Struct *next;
  int val;
}LL_Node;

LL_Node *new_Node(int val){
  LL_Node *ret = (LL_Node*)calloc(1, sizeof(LL_Node));
  ret->val = val;
  ret->next = NULL;
  return ret;
}

LL_Node *insert_Node(LL_Node *head, int val){
  LL_Node *new = new_Node(val);
  if (head == NULL){
    head = new;
  }
  else{
    LL_Node *curr = head;
    while (curr->next != NULL){
      curr = curr->next;
    }
    curr->next = new;
  }
  return head;
}

LL_Node *delete_Node(LL_Node *head){
  if (head == NULL){
    return NULL;
  }
  else{
    LL_Node *new_head = head->next;
    free(head);
    return new_head;
  }
}


void BFS(int adj_mat[5][5], int start_node, int end_node){
  LL_Node *queue = new_Node(start_node);
  int steps = 0;
  while (queue != NULL){
    steps++;
    int curr_node = queue->val;
    queue = delete_Node(queue);
    printf("current node is %d", curr_node);
    for (int i = 0; i < 5; i++){
      if (adj_mat[curr_node][i] == 1){
        if (i == end_node){
          printf("found end after %d", steps);
          return;
        }
        else{
          queue = insert_Node(queue, i);
        }
      }
    }
  }
}

int main(){
  // create adjacency matrix
  int adj_mat[5][5] = {
                      {0,1,0,0,1},
                      {1,0,1,1,1},
                      {0,1,0,0,0},
                      {0,1,0,0,1},
                      {1,1,0,1,0},
  };

  BFS(adj_mat, 2, 4);
  

  return 0;
}
```