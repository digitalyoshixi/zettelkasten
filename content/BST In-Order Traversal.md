---
tags:
  - math
  - linalg
---
```c
void print_Order(Node *node){
	if (node != NULL){
		print_Order(node->left); // print left first
		printf("%p", node);
		print_Order(node->right); //print right later
	}
}
```