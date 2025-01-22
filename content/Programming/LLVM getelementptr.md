---
tags:
  - llvm
aliases:
  - LLVM GEP
---
The pointer arithmetic instruction.
Used to calculate an offset pointer given a value and a struct.

In essence, given a object and a field number, GEP returns the pointer to that object's field at field number.
# Example
```llvm
define ptr @get_inner_in_array(ptr %p, i64 %idx) {
  %q = getelementptr %MyStruct, ptr %p, i64 %idx, i32 1, i32 1
  ret ptr %q
}
```
- Takes an untyped pointer `ptr` into a struct of `%MyStruct` with `ptr %p`
- Take a field number `i64 %idx`
- Firstindex means it starts searching in the `1`st sub-element of `%MyStruct` (assuming that the 1st sub element is an iterable like a list or vector)
- Secondindex means it starts searching at the `1`st sub-element of `%MyStruct.1`
- Return the pointer to the field at field number
# 2019 EuroLLVM Talk Explanation
https://www.youtube.com/watch?v=m8G_S5LwlTo&t=1753s
### First Index Offset
the firstindex only offsets the basetype with [[Pointer Arithmetic]]. This means if the pointer's base-type is int, it offsets pointer by i32. If the pointer's base-type is a 4-integer list, then it offsets by i128 (as 32 * 4 is 128).
![[LLVM getelementptr-20250101040134572.webp]]
![[LLVM getelementptr-20250101040426000.webp]]
### n-th index offset
![[LLVM getelementptr-20250101040714681.webp]]
![[LLVM getelementptr-20250101041052189.webp]]
All subsequent offsets will then be offsets of the inner-element of the first-index's data-type.