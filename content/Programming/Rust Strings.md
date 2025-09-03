---
tags:
  - rust
---
# String 
This is a growable string type that is [[Unicode|UTF-8]] encoded.
```rust
let mut guess = String::new();

```
# Splitting String
```rust
let v: Vec<&str> = "Mary had a little lamb".rsplit(' ').collect();
assert_eq!(v, ["lamb", "little", "a", "had", "Mary"]);
```
