---
tags:
  - programming
  - assembly
---
# Example of 4x4 loop:
```mips
li $t1, 0 # y
li $t2, 0 # x
loop:
    beq $t1, 4, loop_end
    loop_x:
		# BODY
		
		# END
        addi $t2, $t2, 1
        blt $t2, 4 loop_x
    end_x:
        li $t2, 0
        addi $t1, $t1, 1
        j loop_x
loop_end:
    li $t1, 0
```