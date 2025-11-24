---
tags:
  - programming
  - cpp
---
A [[C++ Smart Pointer]] that can be shared across functions.
Uses a reference counter for the number of references, and decrements once a reference goes out of scope.
```cpp
std::unique_ptr<Dog> ralf = std::make_shared<Dog>();
```