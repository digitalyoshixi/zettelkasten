---
aliases: 
tags:
  - cpp
---
# General Runtime Issues
1. ensure these lines are written at the top:
```cpp
#include <iostream>
#include <limits>
```
2. These 2 lines at the end of int main():

```cpp
std::cin.clear(); // reset any error flags
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // ignore any characters in the input buffer until we find an enter character
std::cin.get(); // get one more char from the user
```
This will wait for the user to press a key before continuing on, giving you time to examine the program before the console closes

