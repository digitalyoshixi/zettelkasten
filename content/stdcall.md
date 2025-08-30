---
tags:
  - x86
  - assembly
  - programming
aliases:
  - x86 Function Calls Windows
---
- Callee saved
# Process
1. Arguments are placed onto the stack from left-to-right
2. Function is called with `call <location>`. This causes `rip` to be pushed to the stack (return address)
3. Space is allocated onto the stack for local variables
4. Function does work
5. Stack is restored
6. Returns by calling `ret N` (Returns and removes N arguments)
# Diagram
![[Stack Frame-20250829230239682.webp]]