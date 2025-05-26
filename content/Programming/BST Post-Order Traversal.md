---
tags:
  - c
  - programming
---
1. Visit left subtree
2. Visit right subtree
3. Print data of the node
```c
void print_Order(Node *node){
	if (node != NULL){
		print_Order(node->left); // print left first
		print_Order(node->right); //print right later
		printf("%p", node);
	}
}
```
Useful for [[Parser|Parsing]] [[Abstract Syntax Tree|AST]], or [[BST Delete Tree]]