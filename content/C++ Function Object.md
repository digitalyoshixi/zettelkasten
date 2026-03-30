---
tags:
  - programming
  - c
aliases:
  - C++ Functor
---
[[C++ Objects]] that can be called like a function. They overload the `()` operator.
```cpp
include <iostream>
using namespace std;

class Greet {
  public:    
    // overload function call/parentheses operator
    void operator()() {
      cout << "Hello World!";
    }
};


int main() {
  // create an object of Greet class
  Greet greet;
  // call the object as a function
  greet();
  return 0;
}
```