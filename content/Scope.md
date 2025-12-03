---
tags:
  - programming
  - compilers
---
Handling of what local variables are defined within a  block of code.
Different from a [[Function Closures|Closure]].
If a variable is not found within the current scope, it tries to be found in the scope above this one.
A scope is represented as a [[Chain Map]]