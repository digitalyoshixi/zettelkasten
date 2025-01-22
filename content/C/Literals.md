---
tags:
  - cpp
aliases:
  - Literal Values
---
literal values in source code. fixed values that are directly inserted into memory
```cpp
std::cout << "Hello world!";
int x { 5 };
```
now, if you do something like print a variable with a fixed value, that is not calling a fixed value anymore
```cpp
int x {5};
std::count << x; // not a fixed value, passing a variable
```
because a variable's value is stored in memory, and it can change due to debugging or vulnerabilities.

# Literal Suffixes
like when you want 50f to be a float. They are suffixes you put to assign quick data-types to the literals.

|Data type|Suffix|Meaning|
|---|---|---|
|integral|u or U|unsigned int|
|integral|l or L|long|
|integral|ul, uL, Ul, UL, lu, lU, Lu, LU|unsigned long|
|integral|ll or LL|long long|
|integral|ull, uLL, Ull, ULL, llu, llU, LLu, LLU|unsigned long long|
|integral|z or Z|The signed version of std::size_t (C++23)|
|integral|uz, uZ, Uz, UZ, zu, zU, Zu, ZU|std::size_t (C++23)|
|floating point|f or F|float|
|floating point|l or L|long double|
|string|s|std::string|
|string|sv|std::string_view|