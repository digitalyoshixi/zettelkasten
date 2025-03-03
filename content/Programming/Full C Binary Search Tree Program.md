---
tags:
  - c
---
```c
#include "stdio.h"
#include "stdlib.h"

typedef struct BST_NODE{
  int value;
  struct BST_NODE *left;
  struct BST_NODE *right;
}BST_NODE;


void insert_node(BST_NODE *root, BST_NODE *toadd){
  int target = toadd->value;
  BST_NODE *currentnode = root;
  int added = 0;
  while (added == 0){
    if (currentnode->value > target){
      if (currentnode->left == NULL){
        currentnode->left = toadd;
        added = 1;
      }
      else{
        currentnode = currentnode->left;
      }
    }
    else{
      if (currentnode->right == NULL){
        currentnode->right = toadd;
        added = 1;
      }
      else{
        currentnode = currentnode->right;
      }
    }
  }
}

BST_NODE *create_node(int value){
  BST_NODE *mynode = (BST_NODE*)malloc(sizeof(BST_NODE));
  mynode->value = value;
  mynode->left = NULL;
  mynode->right = NULL;
  return mynode;
}

void print_nodes(BST_NODE* startnode){
  printf("%d\n", startnode->value);
  if (startnode->left != NULL){
    printf("left of %d : ", startnode->value);
    print_nodes(startnode->left);
  }
  if (startnode->right != NULL){
    printf("right of %d : ", startnode->value);
    print_nodes(startnode->right);
  }
}

int main(){
  BST_NODE *root = create_node(10);
  BST_NODE *first = create_node(2);
  BST_NODE *second = create_node(3);
  BST_NODE *third = create_node(5);
  BST_NODE *fourth = create_node(8);
  insert_node(root, first);
  insert_node(root, second);
  insert_node(root, third);
  insert_node(root, fourth);
  print_nodes(root);
  return 0;
}
```