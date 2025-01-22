---
tags:
  - llvm
---
assigns value based on what block we jumped from.
```llvm
phi i32 [0, %start], [%i.new, %loop]
```
means:
- Value should be 0 if we came from `%start` block
- value should be `%i.new` if we came from `%loop` block
This allows you to have dynamic variables
# Alternate Example
```
; After running through `opt -p mem2reg`
define i32 @pow(i32 %x, i32 %y) {
start:
  br label %loop_start

loop_start:
  %i.0 = phi i32 [0, %start], [%i.new, %loop]
  %r.0 = phi i32 [1, %start], [%r.new, %loop]
  %done = icmp eq i32 %i.0, %y
  br i1 %done, label %exit, label %loop

loop:
  %r.new = mul i32 %r.0, %x
  %i.new = add i32 %i.0, 1
  br label %loop_start

exit:
  ret i32 %r.0
}
```