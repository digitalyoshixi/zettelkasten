---
tags:
  - programming
aliases:
  - XOR Trick
---
```cpp
int x = 35;
int y = 67;
x = x^y; //x=96
y = x^y; //x=67
x = x^y; //x=35
```