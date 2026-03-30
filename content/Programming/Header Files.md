---
tags:
  - cpp
aliases:
  - Header File
  - C Header Files
  - C++ Header Files
---
Files ending with `.h` or `.hpp`.
These files allow us to save [[C++ Forward Declaration]] in one file so we can import them in other files.
**You Require the source file with the actual C++ code with this file.** `grades.h` is paired with `grades.cpp`
Implicitly compiled. No need to change your compilation command in command line.
# Writing Header Files
You need:
1. [[Header Guard]]
2. All the [[C++ Forward Declaration]] of the original C++ file that we want other files to see
# Good convention
- Don't write functions or variables inside header files! It breaks [[C++ One Definition Rule|C++ ODR]] during link-time
- Source files should always `#include` their header file
- Do not `#include` `.cpp` files. again [[C++ One Definition Rule|C++ ODR]]
# [[Standard Library]] Header Files
These are header files we have not written and are located at `include directories`, defaulting to the directory the IDE or compiler have declared. 
- You `#include` with `<>` to denote this location.
- You can optionally leave the `.h` in the file name
# Transitive includes
Implicit `#includes` that header files have to include other header files, per sake for dependencies.
# Example

# Concepts
- [[Header Guard]]
- [[Header Only Files]]