---
tags:
  - cpp
  - c
---
Converts a `.c` file into a `.i` file.
Preprocessor is the first stage in the [[C++ Translation]] used to strip code of its un-needed portions.
It:
- Removes comments
- Ensures each file ends with newline
- Fufills [[Preprocessor Directives]] (Literally adds header file code)
- Performs [[C Macro|Macro Substitution]]
