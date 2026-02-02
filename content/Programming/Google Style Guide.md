---
tags:
  - cpp
---
# Link
https://google.github.io/styleguide/cppguide.html
# Traits
- Easy to find
- Cleanly organized
- Concise
- All terms defined
- Examples
# Specifications
- Use `.cc` files
- Every `.cc` file has a corresponding `.h` [[Header Files|Header File]]
- Every header has [[Header Guard]] using `#define`
# Using Style Guide
```
clang-format -style=Google --dry-run myfile.c
```