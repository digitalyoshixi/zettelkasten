---
tags:
  - programming
  - rust
---
This is a [[Rust Enums|Rust Enum]] that can represent a success or error.
```rust
enum Result<T, E>{
	Ok(T),
	Err(E)
}
```