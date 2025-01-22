---
tags:
  - rust
---
If you have a pre-existing struct, you can define functions that the struct datatype can use
```rust
struct Number {
	odd : bool,
	value : i32,
}
impl Number {
	fn isPositive(self){
		self.value > 0;	
	}
}
```