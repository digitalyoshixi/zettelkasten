---
tags:
  - assembly
aliases:
  - MIPS Push
  - MIPS Pop
---
A [[Subroutine|Function]] calling convention that involves pushing and popping arguments onto the [[Stack]]
# Function Call Process
Caller calls callee
1. Caller pushes `$ra` 
2. Caller pushes arguments
3. Callee pops arguments from the stack
4. Callee performs function using temporary variables `$t0,...,$t9`
5. Callee pops `$ra` from the stack
6. Callee pushes return value onto the stack
7. Callee jumps to the return address `$ra`
8. Caller pops return value from stack
9. Caller continues its original logic
# MIPS
Using a [[Stack]], you can push and pop.
### Push
```mips
# push $t0 onto the stack
addi $sp, $sp, -4
sw $t0, 0($sp)
```
### Pop
```mips
# pop from the stack
lw $t0, 0($sp)
addi $sp, $sp, 4
```