---
tags:
  - programming
  - assembly
---
# Example of 4x4 loop:
```mips
li $t1, 0 # y
li $t2, 0 # x
draw_brick_loop:
    beq $t1, 4, end_y
    draw_brick_loop_x:
        beq $t2, 4, end_x
				# BODY
        addi $t2, $t2, 1
        j draw_brick_loop_x
    end_x:
        li $t2, 0
        addi $t1, $t1, 1
        j draw_brick_loop
end_y:
    li $t1, 0
```