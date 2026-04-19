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
# Proof of Height
$minsize(0) = 0$
$\text{minsize}(1) = 1$
Assuming tree is as unbalanced as possible, so one tree end (left or right) is heavier:
- Note that tree size $\text{minsize}(h+2) = \text{minsize}(h)+\text{minsize}(h+1)+1$

Prove by [[Induction]] that $\text{minsize(h)} = fib(h)-1 \frac{\phi^{h+2}-(1-\phi)^{h+2}}{\sqrt{ 5 }}-1$
Note that the [[Fibonacci Series]] grows exponentially by [[Golden Ratio]]
- $\text{minsize}(0) = 0 = 1 - 1 = fib(2)-1 = fib(0+2)-1$
- $\text{minsize}(1) = 1 = 2 - 1 =$
- $$