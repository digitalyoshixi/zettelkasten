---
tags:
  - programming
  - rust
---
This is a library used for generating random numbers.
# Installation
```
cargo add rand
cargo build
```
# Boilerplate
```rust
use rand::Rng;

let secret_number = rand::thread_rng().gen_range(1..=100);
```