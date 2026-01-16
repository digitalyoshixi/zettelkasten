---
tags:
  - programming
  - c
  - memory
aliases:
  - malloc
---
Is a C function to allow memory allocation to the [[OS Heap]].
Requires [[stdlib.h]]
`malloc` syntax is as follows: `(type*)malloc(size_t)`.
- `size_t` - unsigned integer representing size to allocate
- `type*` is what the pointer is typecasted to. 
  It returns pointer as void type automatically, then you can change the type like int* or char* instead of void*. 
Memory addresses can be found by adding # of bytes a datatype has to another address. Reading the data is accessed using pointers. 
# Example
```c
int *ptr = (int*)malloc(5 * sizeof(int));
```
### Malloc for Structs
```c
struct ListNode *retll = (struct ListNode*)malloc(sizeof(struct ListNode) * 2);
```