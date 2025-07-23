---
tags:
  - assembly
  - programming
---
# Starter Code
```mips
.eqv BASE_ADDRESS 0x10008000  
.text  
li $t0, BASE_ADDRESS # $t0 stores the base address for display  
li $t1, 0xff0000 # $t1 stores the red colour code  
li $t2, 0x00ff00 # $t2 stores the green colour code  
li $t3, 0x0000ff # $t3 stores the blue colour code

sw $t1, 0($t0) # paint the first (top-left) unit red.  
sw $t2, 4($t0) # paint the second unit on the first row green. Why $t0+4?  
sw $t3, 256($t0) # paint the first unit on the second row blue. Why +256?  
li $v0, 10 # terminate the program gracefully  
syscall
```