---
tags:
  - programming
  - datatype
---
Returns the value of a corresponding key $k$ in the tree $T$. Exact same as binary search tree
```
search(k,T)
```
# Code
```c
AVL_Node* search(AVL_Node* node, int key) {
  if (node == NULL) return NULL;
  if (key == node->key) return node;
  if (key > node->key) return search(node->right, key);
  return search(node->left, key);
}
```