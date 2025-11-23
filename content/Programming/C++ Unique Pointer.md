---
tags:
  - cpp
---
This is a [[C++ Smart Pointer]] type that provides the caller ownership of the object it points to.

Unique pointers are deleted if the pointer goes out of scope.
```cpp
std::unique_ptr<Dog> ralf = std::make_unique<Dog>();
```
# Getting Raw Pointer
To get the pointer without the uniqueness.
```cpp
std::unique_ptr<Dog> ralf = std::make_unique<Dog>();
ralf.get()
```