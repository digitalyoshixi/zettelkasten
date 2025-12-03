---
tags:
  - cpp
  - programming
---
A form of syntactic ambiguity resolution in [[C++]] where the C++ grammar can't distinguish between creation of object parameter and specification of function type;
```cpp
void f(double my_dbl){
	int i(int(my_dbl));
}
```
- Could either create a variable `i` with value `int(my_dbl)`
- Could call the function `i` with argument `int(my_dbl)`