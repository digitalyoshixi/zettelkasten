---
tags:
  - programming
  - cpp
aliases:
  - C++ Lambda Functions
---
A [[Lambda Function|Anonymous Function]] in [[C++]].
![[C++ Lambda Expressions-20260328233836336.webp]]
```cpp
auto res = [](int x) { return x + x; };
cout << res(5);
```
# Capture Clause
The first segment of a lambda function is its capture clause `[]`.
- `[&]`: capture all external variables by reference
- `[=]`: capture all external variables by value
- `[a, &b]`: capture variable 'a' by value, b by refernce