---
tags:
  - cpp
---
Its a qualifier. Declare `const` before your variables.
example:
```cpp
const double gravity {9.8};
```
# Const function parameters
```cpp
void printInt(const int x)
{
    std::cout << x << '\n';
}
```
You would use this... sometimes...

# [[C++ Macros]] vs Consts
Use constants. macros can be replaced depending on loaded header files.

The opposite to constant is a `volatile` qualifier

# Compile vs Runtime Constants
If a constant has only literal values, then it is a compile-time constant.
If a constant has a value of another variable, that will be resolved during runtime

# constexpr
constant expression makes sure that the current expression is optimized during compile time.
This will only be possible if the circumstances around this is posible. You cannot constexpr a constant which has a volatile value gotten from input or function or other means.
```cpp
constexpr int sum { 4 + 5 };      // ok: 4 + 5 is a constant expression
int age{};
    std::cin >> age;

    constexpr int myAge { age };      // compile error: age is not a constant expression
```
# consteval
consteval is specifically for functions.
If a function can be optimized at compile time, that is, if all the times its used is only with other constants as arguments, then consteval is the keyword to use beforehand to ensure it is compiled at compile-time.
You can also use constexpr, but it may allow it to compile at runtime.