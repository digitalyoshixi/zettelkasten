---
tags:
  - programming
---
Finding height is a $O(\log n)$ operation.
$$
\text{minsize(h)} = \frac{\phi^{h+2}-(1-\phi)^{h+2}}{\sqrt{ 5 }}-1
$$
- With $\phi$ as [[Golden Ratio]]
- With $h$ as the height of the sub tree
# Code
```cpp
int height(AVL_Node* node) {  
  if (node == NULL) return 0;  
  int left = height(node->left);  
  int right = height(node->right);  
  if (left > right) return left + 1;  
  return right + 1;  
}

void updateHeight(AVL_Node* node) { 
	node->height = height(node); 
}  
```