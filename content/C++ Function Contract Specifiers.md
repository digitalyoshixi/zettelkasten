---
tags:
  - programming
  - cpp
---
A specifier for contracts that must be satisfied before the function is ran.
# Specifiers
```cpp
pre(predicate)
post(predicate)
```
# Example
```cpp
int divide(int dividend, int divisor) pre(divisor != 0)
{
    return dividend / divisor;
}
 
double square_root(double num) pre(num >= 0)
{
    return std::sqrt(num);
}

int absolute_value(int num) post(r : r >= 0)
{
    return std::abs(num);
}
```
