---
tags:
  - assembly
  - programming
aliases:
  - MIPS Assembly
---
This is a [[Reduced Instruction Set Compiler|RISC]] instruction set for [[Microprocessor Without Interlocked Pipelined Stages|MIPS]] processors.
- [[Endness|Little Endian]]
# Online Assembler
https://1whatleytay.github.io/saturn
# Boilerplate
```mips
.data
    # TODO: What are the following 5 lines doing?
    promptA: .asciiz "Enter an int A: "
    promptB: .asciiz "Enter an int B: "
    promptC: .asciiz "Enter an int C: "
    resultAdd: .asciiz "A + B = "
    resultSub: .asciiz "A - B = "
    newline: .asciiz "\n"
.globl main
.text
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
# Instructions
### Arithmetic Instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629164312803.webp]]
### Logical Instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629164923738.webp]]
### Shift Instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629164940751.webp]]
### Data Movement Instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629165111177.webp]]
### Load Upper Immediate
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629165133602.webp]]
Loads the [[Immediate]] into the upper half of the register
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629165203658.webp]]
### Arithmetic and Logical [[Pseudo Instructions]]
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250629165519580.webp]]
### Labels
##### Section Labels
Denoted with `labelname: `
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708143554288.webp]]
##### Variable  Labels
Denoted as: `label .type values(s)`
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708154716769.webp]]
### Branches
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708143449492.webp]]
##### Branch PseudoInstructions
Using slt and branch pseudo instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708145918746.webp]]
### Jumps
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708145945191.webp]]
- [[MIPS Jump]]
- [[MIPS Jump and Link]]
### Comparison Instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708150308007.webp]]
- `slt` : 'set less than'
- Stores one if the comparison is true, stores zero otherwise.
### [[Random Access Memory|RAM]] Interactions
These instructions are all [[MIPS Instruction Types|I-Type]]
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708152955129.webp]]
- You are accessing addresses by offsets `i`
- `b` for byte
- `h` for half-[[Binary|Word]]
- `w` for [[Binary|Word]]
- `l` for load
- `s` for store
##### Load and Move Pseudo-Instructions
![[Microprocessor Without Interlocked Pipelined Stages Assembly-20250708155144296.webp]]
- `la` : Load address
- `li` : Load immediate