---
tags:
  - programming
  - datatype
---
### Delete
1. Find the node to delete $v$
	1. Case 1: V has no children: $O(1)$
	2. Case 2: V has one children: $O(1)$
	3. Case 3: V has two children: $O(\log n)$
		1. Find [[Successor Node]] $s$
		2. Replace value of  key value pair of $s$ into $v$
		3. Delete $s$, s's parent adopts $s$ child child
# Code
```c
AVL_Node* delete(AVL_Node* node, int key) {
  if (node == NULL) return NULL;

  if (key < node->key) {
    node->left = delete(node->left, key);
  }

  else if (key > node->key) {
    node->right = delete(node->right, key);
  }

  else {
    if (node->left == NULL) return node->right;
    if (node->right == NULL) return node->left;
    RAVL_Node* succ = successor(node);
    node->key = succ->key;
    node->right = delete(node->right, succ->key);
  }

  updateHeight(node);
  updateSize(node);
  int bf = balanceFactor(node);
  int lbf = balanceFactor(node->left);
  int rbf = balanceFactor(node->right);
  if (bf > 1 && lbf >= 0) return rightRotation(node);
  if (bf < -1 && rbf <= 0) return leftRotation(node);
  if (bf > 1 && lbf < 0) return leftRightRotation(node);
  if (bf < -1 && rbf > 0) return rightLeftRotation(node);
  return node;

```