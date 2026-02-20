---
tags:
  - math
  - data
---
The balance factor is something used to keep balance in a [[AVL Tree]].

$$\text{Balance} = \text{Height(Left Subtreee)} - \text{Height(Right Subtree)}$$
# Balance
- A node $X$ with $BF(X) < 0$ is left heavy
- A node $X$ with $BF(X) > 0$ is right heavy
- A node $X$ with $BF(X) = 0$ is balanced
# Code
```cpp
int height(AVL_Node* node) {  
  if (node == NULL) return 0;  
  int left = height(node->left);  
  int right = height(node->right);  
  if (left > right) return left + 1;  
  return right + 1;  
}

int balanceFactor(AVL_Node* node){
	if (node == NULL) return 0;
	return height(node->left) - height(node->right);
}
```