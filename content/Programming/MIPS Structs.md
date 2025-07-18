---
tags:
  - assembly
---
Implementing [[C Structures]] within [[Microprocessor Without Interlocked Pipelined Stages Assembly|MIPS Assembly]].
They are [[MIPS Arrays]], but with different datatypes.
We can use load and store and offsets
# Boilerplate
Translating:
```c
struct {
	int a;
	int b;
	int c;
} s;
```
```mips
.data
	s: .space 12
.text
.globl main
main:
	la $t0, s
	# storing 5 into s.a
	addi $t1, $zero, 5
	sw $t1, 0($t0)
	# storing 13 into s.b
	addi $t1, $zero, 13
	sw $t1, 4($L0)
	# storing -7 into s.c
	addi $t1, $zero, -7
	sw $t1, 8($t0)
```