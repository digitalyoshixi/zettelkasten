---
tags:
  - math
  - linalg
aliases:
  - Tree Sort
---
1. Visit left subtree
2. Print the node
3. Visit right subtree
```c
void print_Order(Node *node){
	if (node != NULL){
		print_Order(node->left); // print left first
		printf("%p", node);
		print_Order(node->right); //print right later
	}
}
```
# Complexity
- Worst Case: $O(N^{2})$
- Average Case: $O(N)$