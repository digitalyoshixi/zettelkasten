---
tags:
  - c
---
Defining [[C Structures]] as types.
```c
typedef struct some_struct
{
	// entries in the struct
} datatypename;
```
# Example
```c
typedef struct Node {
	int x;
	struct Node *next;
}Node;
```