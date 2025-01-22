---
tags:
  - cpp
---
behavior of some syntax that is left up to the implementation(compiler) to define.
```cpp
#include <iostream>

int main()
{
	std::cout << sizeof(int) << '\n'; // print how many bytes of memory an int value takes

	return 0;
}
```
On some compilers, it will produce `4`, on others it may produce `2`

# Unspecified Behaviors
Very very similar to implementation behaviors, but the implementation is not required to document the behavior. might just be a C++ default difficulty 