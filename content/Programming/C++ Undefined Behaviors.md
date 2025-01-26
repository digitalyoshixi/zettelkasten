---
tags:
  - cpp
---
Undefined behavior(often abbreviated **UB**) is the result of code whose behavior is not well-defined by the C++ language.

C++ may attempt to fix these behaviors on their own. leading to unexpected results such as:
- Program produces different results every time its run
- Program crashes immediately or later
- Program works on some compilers but not others
# Uninitialized Variables
used when you [[Default Initialization]] a variable and don't assign a value to it, it will grab a address of a **random unused** memory location.
```cpp
#include <iostream>
int main()
{
    // define an integer variable named x
    int x; // this variable is uninitialized because we haven't given it a value

    // print the value of x to the screen
    std::cout << x << '\n'; // who knows what we'll get, because x is uninitialized

    return 0;
}
```
For me, this returned the value `779647075`
Later, when i modified that value of memory, by rerunning the program like this:
```cpp
std::cout << x+1 << '\n';
```
the value it returned was `1` and then it was `0` when i reverted the code back to original.
So, it always takes from the same location in memory

Most modern compilers like VScode will detect that there are variables without values and create values in those memory addresses

because this will not issue a warning, it is always good practice tp [[Always Initialize your Variables]]

