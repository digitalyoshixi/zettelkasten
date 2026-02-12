---
tags:
  - programming
  - compilers
aliases:
  - Name Resolution
cssclasses:
---
Handling of what local and global variables are defined within a block of code.
Different from a [[Function Closures|Closure]].
# Name Resolution
1. Checks local function variables
2. If a variable is not found within the current scope, it tries to be found in the scope above this one.
# Types
- [[Lexical Scope]]
- [[Dynamic Scope]]