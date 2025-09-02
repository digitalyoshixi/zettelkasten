---
tags:
  - programming
  - rust
aliases:
  - std::io
---
A input output library
# Boilerplate
```rust
use std::io;

let mut guess = String::new();
io::stdin()
    .read_line(&mut guess)
    .expect("Failed to read line");
```