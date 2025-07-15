---
tags:
  - assembly
---
Arrays are sections of contiguous memory.
They can be of size:
- [[Binary|Word]]
- half word
- byte
- etc
# Boilerplate
```mips
.data  
A: .word 5, 8, -3, 4, -7, 2, 33  # defined array
B: .word 0:7  # array of words, each initialized to 0
LEN: .word 7 # length of the arrays

C: .space 400 # array of 100 integers
D: .word 42:100

.text
main:
	la $t8, C # t8 holds address of array C
	la $t9, D # t9 holds address of array D
	add $t0, $zero, $zero # set $t0 to 0
	addi $t1, $zero, 100 $ t1 holds 100
loop:
	bge $t0, $t1, END # exit loop when i >= 100
	sll $t2, $t0, 2 # $t2 = $t0 * 4 = i * 4 = offset
	add $t3, $t8, $t2 # $t3 = addr(A) + i*4 = Addr(A[i])
	add $t4, $t9, $t2 # $t4 = addr(B) + i*4 = Addr(B[i])
	lw $t5, 0($t4) # $t5 = B[i]
	addi $t5, $t5, 1 # $t5 = $t5 _ 1 = B[i] + 1
	sw $t5, 0($t3) # A[i] = $t5
UPDTE:
	addi $t0, $50, 1
	j loop
END: ...
```
# Iterating Through Array
accessing `A[4]` is `A + 4*4`. where 4 is the word-size, and 4 is the offset.