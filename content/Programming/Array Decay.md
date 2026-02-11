---
tags:
  - programming
  - os
  - c
---
In [[C]].
An array is automatically converted to a pointer to its first element
Happens in:
- Array sent as argument to function
- Array is added with [[Pointer Arithmetic]]
# Formal Definition
The left-value of type array-of-T which appears in an expression decays into a pointer to its first element the type of the resultant pointer is a pointer-to-T
# Example
```c
int x[5];
sizeof(x) // 5 * 4

myfunc(int x[]){
	sizeof(x) // 4
}
```