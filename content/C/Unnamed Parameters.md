---
tags:
  - cpp
---
when parameter name not given within function declarator
```cpp
int somefunc(int){ // no fucking parameter name
	return 2;
}
```
The only reason you would use this is to implement virtuals from a base class that must match the same # of parameters
https://www.learncpp.com/cpp-tutorial/introduction-to-function-parameters-and-arguments/