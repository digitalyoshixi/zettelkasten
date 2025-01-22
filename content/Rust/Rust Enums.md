---
tags:
  - rust
---
```rust
enum Option<T> {
	None,
	Some(T)
}
```
or 
```rust
enum Result<T, E>{
	Ok(T),
	Err(E)
}
```