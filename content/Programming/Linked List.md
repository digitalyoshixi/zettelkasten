---
tags:
  - programming
  - c
aliases:
  - List
  - Singly Linked List
  - Double Linked List
  - Circular Linked List
---
A list made of node structures that point to the address of the subsequent list element.
Each linked list comes with an independent variable `head` that points to the first node in the list.
# Types
### Single Linked List
You can only go forward because each node only has 1 pointer.
```c
typedef struct node{
	int data;
	struct node *next;
}node;
```
### Double Linked List
Points to forward node and behind node
### Circular Linked List
Last element is linked to first element. Thus no pointer points to NULL
### [[Embedded Doubly Linked Lists]]
# Guides
- [[C Linked List Traversal]]
- [[C Linked List Deletion]]
- [[C Linked List Reversal]]