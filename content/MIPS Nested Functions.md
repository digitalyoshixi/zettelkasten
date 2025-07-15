---
tags:
  - assembly
  - programming
aliases:
  - MIPS Recursive Functions
---
For nested functions we have to ensure the return address of the last function is saved onto the stack.
# Boilerplate
```mips
.data
    introString: .asciiz "Enter a number: "
    resultString: .asciiz "The result is: "
    newLine: .asciiz "\n"

.globl main
.text 
    main:
        # print the intro stirng
        li $v0, 4
        la $a0, introString
        syscall
        # read a number
        li $v0, 5
        syscall
        move $a0, $v0 #a0 holds our input
        # call the function
        function_setup:
            # push a0 onto the stack
            addi $sp, $sp, -4
            sw $a0, 0($sp)
        jal mystery
        # print the result string
        li $v0, 4
        la $a0, resultString
        syscall
        # pop the return value from the stack
        lw $t0, 0($sp)
        addi $sp, $sp, 4
        move $a0, $t0
        # print a integer
        li $v0, 1
        syscall

    exit: 
        li $v0, 10
        syscall

    mystery: 
        # pop the arguments off the stack
        lw $t0, 0($sp)
        addi $sp, $sp, 4
        bne $t0, $zero, mystery_recurse
        
        mystery_base:
            # return 1, and push this as the return value
            li $t0, 1
            addi $sp, $sp, -4
            sw $t0, 0($sp)
            jr $ra
            
        mystery_recurse: # mystery(n-1) + 2n - 1
            # store the value of 2n onto the stack
            add $t1, $t0, $t0
            addi $sp, $sp, -4
            sw $t1, 0($sp)
            # store the value of $ra onto the stack
            move $t1, $ra
            addi $sp, $sp, -4
            sw $t1, 0($sp)
            # store the value of n-1 onto the stack
            sub $t0, $t0, 1
            addi $sp, $sp, -4
            sw $t0, 0($sp)
            
            # call the mystery function with recursive again
            jal mystery

            # pop the return value off of the stack
            lw $t0, 0($sp)
            addi $sp, $sp, 4
            # pop $ra off the stack
            lw $t1, 0($sp)
            addi $sp, $sp, 4
            # pop the value of 2n off the stack
            lw $t2, 0($sp)
            addi $sp, $sp, 4
            # compute the return value
            add $t0, $t0, $t2
            sub $t0, $t0, 1
            # push result onto stack
            addi $sp, $sp, -4
            sw $t0, 0($sp)
            # return
            jr $t1
```