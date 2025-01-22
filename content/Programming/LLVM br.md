---
tags:
  - llvm
---
### `br il <condition>, label %branch1, label %branch2`
A branch statement that changes execution point depending on condition.
```c
define i64 @safe_div(i64 %n, i64 %d) {
  %1 = icmp eq i64 %d, 0
  br i1 %1, label %iszero, label %nonzero

iszero:
  ret i64 -1

nonzero:
  %2 = udiv i64 %n, %d
  ret i64 %2
}
```
br with one branch is equivalent to an unconditional `goto`
```c
br il %1, label %gohere

gohere:
	ret i64 0
```