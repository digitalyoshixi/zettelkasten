---
tags:
  - ARM
  - assembly
---
They follow the structure: operation [operands,..]

| operation                                | example        | explanation                                                                                                               |
| ---------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------- |
| mov (move)                               | mov ebx, 123   | ebx = 123                                                                                                                 |
|                                          | Mov eax, ebx   | eax = ebx                                                                                                                 |
| add                                      | add ebx, ecx   | ebx += ecx                                                                                                                |
| adc                                      | adc ebx, ecx   | ebx += ecx BUT if (ebx + ecx) > 0xFFFFFFFF, then it carries the remainder in cpsr.TLDR: ebx = ecx 100% regardless of size |
| sub                                      | sub ebx, edx   | ebx -= edx                                                                                                                |
|                                          | sub r2,r1,r0   | r2 = r1-r0                                                                                                                |
| subs                                     | subs r2,r1,r0  | r2 = r1-r0 BUT it keeps negative sign                                                                                     |
| mul (multiply)                           | mul ebx        | eax = ebx                                                                                                                 |
| div                                      | div edx        | eax /= edx                                                                                                                |
| swi (software interrupt)                 | swi 0          | Software interruption. Check if program ends                                                                              |
| ldr (stack->register)                    | ldr r0,=list   | r0 = data at list                                                                                                         |
|                                          | ldr r1,[r0]    | r1 = data at address of r0                                                                                                |
|                                          | ldr r2,[r0,#4] | r1 = data at address of r0+4                                                                                              |
| str (register->stack)                    | Str r1,[r0]    | Store value of r1 into the location of r0.                                                                                |
| and                                      | and r0,r1,r2   | r0 = r1 and r2                                                                                                            |
|                                          | And eax,0xFC   | Clear eax registry(unless 0xFC values exist)                                                                              |
| orr (or)                                 | orr r0,r1,r2   | r0 = r1 or r2.                                                                                                            |
| eor (xor)                                | eor r0,r1,r2   | r0 = r1 xor r2                                                                                                            |
| mvn (move negative)                      | mvn r0,r0      | r0 = not r0 Move to source and negate. A true would turn false                                                            |
| lsl (logical left shift)                 | lsl r0,#1      | Logical left r0 one time                                                                                                  |
| rsl (logical right shift)                | rsl r0,#2      | Logical right r0 2 times                                                                                                  |
| lsr (rotational left shift)              | lsr r0,#1      | Rotational left r0 one time                                                                                               |
| rsr (rotational left shift)              | rsr r0,#2      | rotational right r0 2 times                                                                                               |
| cmp (compare)                            | cmp r0,r1      | Compare r0 and r1. Opens up the door for branches                                                                         |
| bgt (branch if greater than)             | bgt some_label | Will branch if previous compare have first value larger than second into some_label function                              |
| bge (branch if greater than or equal to) | bge some_label | branches to another label if previous compare’s 1st arg is greater or equal to 2nd arg                                    |
| bal (branch always)                      | bal some_label | Unconditionally branch to this label. unavoidable                                                                         |
| blt (branch less than)                   | blt some_label | Branches if 1st argument is smaller than second argument                                                                  |
| beq                                      | beq some_label | Branches if both arguments are equal                                                                                      |
| bne)                                     | bne some_label | Branches if both arguments not equal                                                                                      |
| bx (branch to register)                  | bx lr          | Branch to linked register                                                                                                 |
| bl (branch label)                        | bl some_label  | Branch to some label                                                                                                      |
| push (push onto stack)                   | push {r0,r1}   | Push r0 and r1 into stack                                                                                                 |
| pop (pop from stack)                     | pop {r0,r1}    | Retireve r0 and r1 from the stack                                                                                         |
# Chaining operations
Certain operations can be completed in tandem with other operations. An example being move and logical shift
mov r1,r0,lsl #1
will first assign r1 to r0 and then logical shift it by one