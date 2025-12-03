---
tags:
  - programming
  - compilers
aliases:
  - Generic
  - Generic IR
---
A [[Intermediate Representation|IR]] used by [[GCC]].
Common for all frontends.
# Example
```cpp
int f(int x){
	int y = 0;
	if (x>0)
		y = 4*x*x + 1;
	return y;
}
```
Converts to:
```cpp
{
	int y = 0;
	if (x>0){
		y = (x*x) * 4 + 1;
	}
	return y;
}
```
Notice:
- [[Reassociation of Expressions]]