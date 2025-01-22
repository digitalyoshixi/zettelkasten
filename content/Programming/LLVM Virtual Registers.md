---
tags:
  - llvm
---
These are 'variables' in the sense that they are infinite, but the LLVM backend maps them to use CPU registers for computations.
LLVM allows for an infinite set of virtual registers labeled from `%0`, `%1`, `%2`, ...
# Custom Named Registers
By default, registers are numbered, `%0`, `%1`, but you can give them custom names like:
`%myvar`, `%subresult`, etc