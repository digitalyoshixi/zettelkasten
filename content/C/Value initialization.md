---
tags:
  - cpp
---
```cpp
int f {};      // initializer is empty braces (value initialization)
```
value will be set to 0 when this happens. this is zero initialization

# manually setting 0 vs {}
```cpp
int x {0};
int x{};
```
above does the same thing

Use explicit zero initialization when you are actually using zero.
Use Value initialization when the value is temporary and will be replaced.
