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
# Methods
### .expect("message")
- If the result returned `Err(E)`, then the program will crash and display string
- If the result returned `Ok(T)`, expect will return the value within `Ok(T)`