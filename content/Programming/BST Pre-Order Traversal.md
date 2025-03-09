---
tags:
  - c
  - programming
---
1. Print data of the node
2. Visit left subtree
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