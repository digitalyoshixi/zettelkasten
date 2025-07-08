---
tags:
  - assembly
---
```mips
.data
    # TODO: What are the following 5 lines doing?
    promptA: .asciiz "Enter an int A: "
    promptB: .asciiz "Enter an int B: "
    promptC: .asciiz "Enter an int C: "
    resultAdd: .asciiz "A + B = "
    resultSub: .asciiz "A - B = "
    newline: .asciiz "\n"
.text
.globl main
    main:
    # Syscall 4, printing the value of promptA to the screen
    li $v0, 4
    la $a0, promptA
    syscall
    # Read an integer into $t0
    li $v0, 5
    syscall
    move $t0, $v0
    # Print promptB
    li $v0, 4
    la $a0, promptB
    syscall
    # Get number and store into $t1
    li $v0, 5
    syscall
    
    move $t1, $v0
    # Store the sum of t1 and t0 into t3
    add $t2, $t1, $t0
    # store the subtraction of t0 from t1 into t3
    sub $t3, $t0, $t1
    # print the add string
    li $v0, 4
    la $a0, resultAdd
    syscall
    # print the value of the add
    li $v0, 1
    move $a0, $t2
    syscall
    # print new line
    li $v0, 4
    la $a0, newline
    syscall
    # print the subtract string
    li $v0, 4
    la $a0, resultSub
    syscall
    # print the subtracted value
    move $a0, $t3
    li $v0, 1
    syscall
    # print newline
    li $v0, 4
    la $a0, newline
    syscall
    # end syscall
    li $v0, 10
    syscall
```