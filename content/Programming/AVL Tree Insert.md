---
tags:
  - programming
  - datatype
---
# Insert
1. Find the node to become parent of the new node
2. Put new node in there
3. Rebalance and update heights if needed
Time complexity $O(\log n)$
# Code
```c
AVL_Node* insert(AVL_Node* node, int key, void* value) {
  if (node == NULL) {
    return createNode(key, value);
  }

  if (node->key < key) {
    node->right = insert(node->right, key, value);
  }

  else {
    node->left = insert(node->left, key, value);
  }
  updateHeight(node);
  updateSize(node);

  int bf = balanceFactor(node);

  if (bf > 1 && key < node->left->key) {
    return rightRotation(node);
  }
  if (bf < -1 && key > node->right->key) {
    return leftRotation(node);
  }
  if (bf > 1 && key > node->left->key) {
    return leftRightRotation(node);
  }
  if (bf < -1 && key < node->right->key) {
    return rightLeftRotation(node);
  }
  return node;
}
```

