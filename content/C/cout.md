---
tags:
  - IO
  - cpp
aliases:
  - std::cout
---
character output. outputs data back out the console in text

```cpp
#include <iostream>
int main(){
	std::cout << "hi"; // hi
	std::cout << 5; // 5
	int xmeg {231};
	std::cout xmeg; // 231
	std::cout << "Your age is: " << xmeg; // Your age is 231
	return 0;
}
```

std::cout is often paired with [[endl|std::endl]]
