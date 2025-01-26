---
tags:
  - cpp
---
Programs are runable binaries created through **multiple** files

# Creation
I have 2 files
```cpp
// add.cpp
int add(int x, int y)
{
    return x + y;
}
```
```cpp
// main.cpp
#include <iostream>

int add(int x, int y); // needed so main.cpp knows that add() is a function defined elsewhere

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}
```
make sure to have the [[C++ Forward Declaration]] for the other file's functions
then compile with 
`g++ -o main main.cpp add.cpp `
