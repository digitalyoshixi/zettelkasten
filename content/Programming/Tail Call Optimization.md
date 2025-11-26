---
tags:
  - llvm
  - compilers
---
An optimization technique that attempts to reduce creation of stack frames by passing literals in expressions as arguments into the function so that the return value does not need to be held.
# Example
![[Tail Call Optimization-20251126001956281.webp]]
# [[GCC]] Command
`-tailcallelim`