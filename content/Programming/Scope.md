---
tags:
  - programming
  - compilers
aliases:
---
Handling of what local variables are defined within a block of code.
Different from a [[Function Closures|Closure]].

A scope is represented as a [[Chain Map]]
# Scoping
1. Checks local function variables
2. If a variable is not found within the current scope, it tries to be found in the scope above this one.