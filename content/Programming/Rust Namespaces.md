---
tags:
  - rust
---
These are imported module spaces.
You can access methods from these namespaces.
# Accessing Fields
```rust
let least = std::cmp::min(3,9);
```
# Bringing Namespaces to Scope
```rust
use std::cmp:min;

let least = min(3,9);
```
# Namespaces and Default Methods
It is important to know that some methods have a namespace equivalent function.
```rust
let x = "amos".len();
let x = std::len("amos");
```