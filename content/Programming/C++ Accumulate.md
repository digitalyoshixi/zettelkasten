---
tags:
  - programming
  - cpp
aliases:
  - C++ Fold
---
A [[Racket fold|fold]] function for [[C++]]
```cpp
T accumulate(InputIt first, InputIt last, T init)
```
# Usage
```cpp
std::vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
 
int sum = std::accumulate(v.begin(), v.end(), 0);
```