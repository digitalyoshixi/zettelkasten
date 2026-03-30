---
tags:
  - cpp
---
# The problem
We need to avoid accidental double declarations.
This may occur if we create a function inside a code that references the header file to a source code with the same function.

# Solution
Put `#pragma once` at the start of each header file.
This is what `#pragma once` does:
```cpp
#ifndef SOME_UNIQUE_NAME_HERE
#define SOME_UNIQUE_NAME_HERE

// your declarations (and certain types of definitions) here

#endif
```
