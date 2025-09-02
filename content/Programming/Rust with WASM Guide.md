---
tags:
  - programming
  - rust
  - wasm
---
# Guide
1. Setup a project with [[Cargo]]
```
cargo new myproject
```
2. `cd myproject`
3. `cargo build`
4. We need [[wasm-bindgen]] and [[wasm-pack]]
```
cargo add wasm-bindgen
```
```
cargo install wasm-pack
```
5. Create a file `src/lib.rs`
```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn add(a : i32, b : i32) -> i32 {
    a+b
}
```
6. 
```
wasm-pack build --target web
```
7. The exported [[WASM Module]] should be in `pkg/myfile.wasm`, and JS files should be created for loading
8. Create a `index.html` with:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body >
    <script type="module">
      import init, {add} from "./pkg/hello_wasm.js"
      // setup glue code
      await init()
      console.log(add(1,2))
    </script>
  </body>
</html>
```
9. Run with [[Python HTTP Server]]
```
python -m http.server
```