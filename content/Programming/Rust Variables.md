---
tags:
  - rust
aliases: []
---
# Dynamic Type Annotation
```rust
let x = 42;
```
# Explicit Type Annotation
```rust
let x : i32 = 42;
```
# Thrown Variables
Variables that have their values thrown away immediately after.
```rust
// throw away the result of somefunc()
let _ = somefunc();
```

# Mutability
By default, all variables in rust are immutable. To make something mutable you must use the `mut` keyword.
```rust
let mut doorstatus = false;
doorstatus = true;
```