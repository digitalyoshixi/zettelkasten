---
tags:
  - c
---
Defining [[C Structures]] as types.

```c
typedef struct Node {
	int x;
	struct Node *next;
}Node;
```