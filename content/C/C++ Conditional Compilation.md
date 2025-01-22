---
tags:
  - cpp
---
# Table of Contents
```table-of-contents
```
# Conditional Compilation
Allows fine-tuning over what to compile and what not.
Utilizes:
- `ifdef`
- `ifndef`
- `endif`
**ifdef**: checks a condition if true to continue compiling before the next `endif`
**ifndef**: checks a condition if false to continue compiling before `endif`

**ifdef and ifndef** can both be replaced with `if defined(arg)` and `if !defined(arg)` respectively and both can be used as [[Preprocessor Directives]]
### ifdef Example
```cpp
#include <iostream>

#define PRINT_JOE

int main()
{
#ifdef PRINT_JOE
    std::cout << "Joe\n"; // will be compiled since PRINT_JOE is defined
#endif

#ifdef PRINT_BOB
    std::cout << "Bob\n"; // will be excluded since PRINT_BOB is not defined
#endif

    return 0;
}
```
### ifndef Example
```cpp
#include <iostream>

int main()
{
#ifndef PRINT_BOB
    std::cout << "Bob\n";
#endif

    return 0;
}
```
### if 0
used as comments to block lines of code from compilation
```cpp
#include <iostream>

int main()
{
    std::cout << "Joe\n";

#if 0 // Don't compile anything starting here
    std::cout << "Bob\n";
    std::cout << "Steve\n";
#endif // until this point

    return 0;
}
```
temporarily 'remove' the comment by changing it to `if 1`
