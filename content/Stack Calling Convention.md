---
tags:
  - assembly
---
A [[Subroutine|Function]] calling convention that involves pushing and popping arguments onto the [[Stack]]
# MIPS
Using [[MIPS Stack]], you can push and pop.
### Push
```mips
# push $t0 onto the stack
sub $sp, $sp, 4
sw $t0, 0($sp)
```
### Pop
```mips
# pop from the stack
lw $t0, 0($sp)
add $sp, $sp, 4
```