---
tags:
  - programming
---
```cpp
int size(AVL_Node* node) {  
  if (node == NULL) return 0;  
  return 1 + size(node->left) + size(node->right);  
}
```
