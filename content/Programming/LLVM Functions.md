---
tags:
  - llvm
---
# Definitions
### Return Nothing Function
```c
define void @do_nothing() {
	ret void
}
```
- Return type is void
- Returns void
- Starts with a `@` which is a [[LLVM Sigil]]
### Function That Takes Arguments and Returns
```c
define i32 @square(i32 %x) {
	%1 = mul i32 %x, %x
	ret i32 $1
}
```
- `%1` is a register that is in i32 type,
- `mul` is a [[LLVM Operations]] that multiplies `$x` with `$x`
# Function Calls
```
%result = call i32 @my_func(i32 %x)
```