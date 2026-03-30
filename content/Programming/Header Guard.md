---
tags:
  - cpp
---
Used to avoid double declarations of a header file.
# C
Name does not matter, just be consistent.
```c
#ifndef SOME_UNIQUE_NAME_HERE
#define SOME_UNIQUE_NAME_HERE

// body

#endif
```
# C++
Put `#pragma once` at the start of each header file.

This is what `#pragma once` does:
```cpp
#ifndef SOME_UNIQUE_NAME_HERE
#define SOME_UNIQUE_NAME_HERE

// your declarations (and certain types of definitions) here

#endif
```