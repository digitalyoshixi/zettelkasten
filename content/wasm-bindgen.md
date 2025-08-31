---
tags:
  - programming
  - rust
  - wasm
aliases:
  - Rust WASM
---
This is a [[Rust]] package used to indicate exports in rust code for the [[WASM Module]].
Uses [[Procedural Macro]].
[[wasm-pack]] can build after you make the file
# Install
```
cargo add wasm-bindgen
```
# Boilerplate
```rust
mod utils;

use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet() {
    alert("Hello, wasm-on-web!");
}
```
