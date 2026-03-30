---
tags:
  - cpp
---
A [[C++ Attribute Specifier]]
To prevent warnings from occuring due to unused variables, before the variable type \[\[maybe_unused\]\]
```cpp
int main()
{
    [[maybe_unused]] double pi { 3.14159 };
    [[maybe_unused]] double gravity { 9.8 };
    [[maybe_unused]] double phi { 1.61803 };

    // the above variables will not generate unused variable warnings

    return 0;
}
```
