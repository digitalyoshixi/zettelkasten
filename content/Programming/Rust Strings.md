---
tags:
  - rust
---
# Splitting String
```rust
let v: Vec<&str> = "Mary had a little lamb".rsplit(' ').collect();
assert_eq!(v, ["lamb", "little", "a", "had", "Mary"]);
```
