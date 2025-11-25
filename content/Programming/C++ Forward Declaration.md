---
tags:
  - cpp
aliases:
---
if you are using a function in another function, declare that function before you call it
```cpp
#include <iostream>
// NOTICE! WRITTEN BEFORE MAIN() METHOD
int add(int x, int y)
{
    return x + y;
}

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}
```
alternatively, you can use forward declaration
```cpp
#include <iostream>
// forward declaration
int add(int x, int y);

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}
// posthastly declared
int add(int x, int y)
{
    return x + y;
}
```
