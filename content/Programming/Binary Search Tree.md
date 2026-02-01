---
tags:
  - programming
aliases:
  - BST
---
A type of [[Tree]] created specially for [[Binary Search]].
# Requirements
- Requires a BST constraint which is a condition to enforce if target value does not match the value at the current node. (E.G, $<$ : go left node, $\geq$ : go right node)
- Each node must have a 'key' value
- Each node must be unique
# Creation Process
1. Given a unsorted input list $[\dots]$
2. Set the root node as the first element of the input list
3. With the subsequent elements of the input list, following the BST constraint to add this element as a node to the tree.
![[Binary-search-tree-insertion-animation.gif]]
# C Implementation
```c
typedef struct BST_Node{
	int value;
	struct BST_NODE *left;
	struct BST_NODE *right;
}BST_NODE
```
- [[Full C Binary Search Tree Program]]
# Operaitons
- [[BST Insertion]]
- [[BST Deletion]]
- [[BST Delete Tree]]
- [[BST In-Order Traversal]]
- [[BST Pre-Order Traversal]]
- [[BST Post-Order Traversal]]
- [[Balanced BST]]