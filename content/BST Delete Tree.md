---
tags:
  - c
  - programming
---
1. Enter left tree
2. Enter right tree
3. Delete current node
# Implementation
```c
void delete_BST(BST_Node *root)
{
  if (root!=NULL)
  {
    delete_BST(root->left);
    delete_BST(root->right);
    printf("deleting node with %f\n", root->key);
    free(root);
  }
}
```