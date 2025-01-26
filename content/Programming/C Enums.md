---
tags:
  - c
---
Ways to assign integers to names.
Instead of:
```c
int a = 0;
int b = 1;
int c = 2;
```
You create an enum that is:
```c
enum Example
{
	A = 0, B = 1, C = 2
};

Example a = A;
```
Useful for using integers as states.