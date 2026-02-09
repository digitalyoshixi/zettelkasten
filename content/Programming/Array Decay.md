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
# Example
```c
int x[5];
sizeof(x) // 5 * 4

myfunc(int x[]){
	sizeof(x) // 4
}
```