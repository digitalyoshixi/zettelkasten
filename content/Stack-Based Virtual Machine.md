---
tags:
  - programming
  - compilers
---
A [[Virtual Machine]] that does not have [[Register]] or intermediate variables.
All data is pushed and popped from the stack
# Example
For interpreting [[Web Assembly Text|WAT]]
1. Push $a onto the stack
   ![[Stack-Based Virtual Machine-20250831124616520.webp]]
2. Push $b onto the stack
   ![[Stack-Based Virtual Machine-20250831124627136.webp]]
3. Pop \$a and \$b
   ![[Stack-Based Virtual Machine-20250831124639712.webp]]
4. Push the result onto the stack
   ![[Stack-Based Virtual Machine-20250831124647640.webp]]