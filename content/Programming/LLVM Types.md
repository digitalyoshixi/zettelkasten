---
tags:
  - llvm
---
# Numbers
- `i32` - most commonly used 32-bit integer
- `i1` - 1-bit integer used for **booleans**
- `float` - single-precision 32-bit float
- `double` - double-precision 64-bit float
- `bfloat` - [[LLVM Brain floating point]]. special operatons
# Void
- `void` - used as return types
# Pointers
- `ptr` - general purpose untyped pointer
# Pseudo-Types
- `label` - pseudo-type that represents block label. see [[LLVM Label]]
- `token`
- `metadata`
# Arrays
- `[<number> x <Type>]`. Examples include:
	- `%myarr = [1024 x i8]`
	- `%myzeroarr = [0 x i32]`
# Structs
- `{<Type1>, <Type2>, ...}`. Examples include:
	- `{i64, ptr}`
- `<{...}>` is a packed struct.
# Vectors
- `<<number> x <Type>>`. Examples include:
	- `%myvec = <4 x i32>`
# Types
- `type` can be used to define new types.
```
%slice = type {i64, ptr}
```