---
tags:
  - x86
  - assembly
---
# [[C]] Boilerplate Decompilation
```c
push rbp // push the main function to stack
mov rbp,rsp // sets up new stack frame for main function
sub rsp,0x10 // Allocate 16 bytes of stack space for local variables
mov DWORD PTR [rbp-0x4],edi // stores first argument 'argc' onto stack
mov QWORD pTR [rbp-0x10],rsi // stores second argument `argv` onto stack
mov    rax, qword ptr fs:[0x28] // generate stack canry
mov    qword ptr [rbp - 0x18], rax // store canary on stack
xor    eax, eax

...

mov    eax,0x0 // return 0;
leave // pops old frame pointer off stack
ret // returns to main's initial address
```
# Instructions
### Essential
- [[x86 mov]]
- [[x86 lea]]
- [[x86 nop]]
### Arith & Logic
- [[x86 add]]
- [[x86 sub]]
- [[x86 inc]]
- [[x86 dec]]
- [[x86 mul]]
- [[x86 div]]
- [[x86 imul]]
- [[x86 idiv]]
- [[x86 and]]
- [[x86 or]]
- [[x86 xor]]
- [[x86 shl]]
- [[x86 shr]]
- [[x86 rol]]
- [[x86 ror]]
### Function
- [[x86 push]]
- [[x86 pop]]
- [[x86 call]]
- [[x86 leave]]
- [[x86 enter]]
- [[x86 ret]]
### Conditional
- [[x86 test]]
- [[x86 cmp]]
### Branching
- [[x86 jmp]]
### String/Rep Instructions
# Notation
- [[x86 Variable Dereferencing]]

| operation               | Intel Syntax  | pseudo demo                                                 |
| ----------------------- | ------------- | ----------------------------------------------------------- |
| mov (move)              | mov ebx, 123  | ebx = 123                                                   |
|                         | Mov eax, ebx  | eax = ebx                                                   |
| add                     | add ebx, ecx  | ebx += ecx                                                  |
| sub                     | sub ebx, edx  | ebx -= edx                                                  |
| mul (multiply)          | mul ebx       | eax \*= ebx                                                 |
| div                     | div edx       | eax /= edx                                                  |
| int (interrupt)         | Int 0         | Check if program ended                                      |
|                         | int 0x80      | System call. Check if eax and abx register have cool values |
| jmp (jump)              | jmp some_addr | Changes RIP to the address                                  |
| nop(no operation)       | nop           | Do nothing                                                  |
| cmon (conditional move) | cmov ecx, eax | if ecx has the value true, then move address stored in eax  |