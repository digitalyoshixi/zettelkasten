---
tags:
  - proofs
---
# Case 1 - Leaf
Delete the leaf and you are done
# Case 2 - Node with 1 child
Swap the parent of the node with the child node, and then remove the original node
# Case 3 - Node with 2 children
1. Find the smallest in the right subtree of the node
   ![[BST Deletion-20250305163425668.webp|344]]
   Go to the right subtree then continue going down the left branch
2. Replace the node to delete with the one you found
   ![[BST Deletion-20250305163544112.webp|279]]
# C Implementation
```c
#include <stdio.h>
#include <stdlib.h>


typedef struct BST_Node_Struct{
  struct BST_Node_Struct *left;
  struct BST_Node_Struct *right;
  int key;
}BST_Node;

BST_Node *new_node(int key){
  BST_Node *ret = (BST_Node*)calloc(1, sizeof(BST_Node));
  ret->key = key;
  ret->left = NULL;
  ret->right = NULL;
  return ret;
}

BST_Node *insert(BST_Node *root, int key){
  BST_Node *new = new_node(key);
  if (root == NULL){
    return new;
  }
  if (root->key == key){
    return root;
  }
  else{
    if (key < root->key){
      root->left = insert(root->left, key);
    }
    if (key > root->key){
      root->right = insert(root->right, key);
    }
  }
  return root;
}

BST_Node *search(BST_Node *root, int key){
  if (root == NULL){
    return NULL;
  }
  if (key == root->key){
    return root;
  }
  if (key < root->key){
    return search(root->left, key);
  }
  else{
    return search(root->right, key);
  }
}

BST_Node *find_parent(BST_Node *root, BST_Node *target){
  if (root == NULL){
    return NULL;
  }
  if (root->left == target || root->right == target){
    return root;
  }
  if (target->key < root->key){
    return find_parent(root->left, target);
  }
  else{
    return find_parent(root->right, target);
  }
}

BST_Node *delete(BST_Node *root, int key){
  // search for the node
  BST_Node *target = search(root, key);
  if (target == NULL){
    return root;
  }
  else{
    if (target->left == NULL && target->right == NULL){
      printf("FIRST\n");
      BST_Node *parent = find_parent(root,target);
      if (target->key < parent->key){
        parent->left = NULL;
      }
      else{
        parent->right = NULL;
      }
      free(target);
      return root;
    }
    // only one child (left)
    else if (target->right == NULL){
      printf("SECOND\n");
      target->key = target->left->key;
      target->left = NULL;
      free(target->left);
      return root;
    }
    // only one child (right)
    else if (target->left == NULL){
      printf("THIRD\n");
      target->key = target->right->key;
      target->right = NULL;
      free(target->right);
      return root;
    }
    // two children (find successor)
    else{
      printf("FOURTH\n");
      // find successor 
      BST_Node *successor = root->left;
      while (successor->right != NULL){
        successor = successor->right;
      }
      int succ_key = successor->key;
      target = delete(target, successor->key);
      target->key = succ_key;
      return root;
    }
  }
}

void in_order(BST_Node *root){
  if (root != NULL){
    in_order(root->left);
    printf("%d,", root->key);
    in_order(root->right);
  }
}

void pre_order(BST_Node *root){
  if (root != NULL){
    printf("%d,", root->key);
    in_order(root->left);
    in_order(root->right);
  }
}

void post_order(BST_Node *root){
  if (root != NULL){
    in_order(root->left);
    in_order(root->right);
    printf("%d,", root->key);
  }
}
int main(){
  BST_Node *root = new_node(20);
  root = insert(root, 14);
  root = insert(root, 54);
  root = insert(root, 26);
  root = insert(root, 8);
  root = insert(root, 17);
  root = insert(root, 30);
  printf("%p\n", search(root, 14));
  printf("%p\n", find_parent(root, search(root, 14)));
  in_order(root);
  printf("\n");
  root = delete(root, 14);
  in_order(root);
  printf("\n");
  return 0;
}
```