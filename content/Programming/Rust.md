---
tags:
  - rust
---
A Low-level systems programming language that allows for memory safety.
# Installation
 [[Rustup]] (recommended)
### Alternate Installation
`sudo pacman -S rust rust-cargo`
# Compile and Run (rustc)
1. `rustc file.rs`
2. `./file`
# Project Setup (cargo)
1. `cargo new <projectname>` or `cargo init`
2. After writing all files, do `cargo build`
3. `cargo run` will run the .rs file in `/src`
# Concepts
### Tools
- [[Cargo]]
- [[Rustup]]
- [[Rustc]]
### Foundation
- [[Rust Variables]]
- [[Rust Mutability]]
- [[Rust Tuple]]
- [[Rust Functions]]
- [[Rust Conditional Statements]]
- [[Rust Match]]
- [[Rust Namespaces]]
- [[Rust Structs]]
	- [[Rust Struct Implementation]]
- [[Rust Vector]]
- [[Rust Macro]]
- [[Rust Enums]]
- [[Rust Iterators]]
- [[Rust Strings]]
### Errors & Handling
- [[Rust Panic]]
- [[Rust Expect]]
- [[Rust Result]]
- [[Rust ?]]
- [[Rust Allow Unused Variables]]
### Extra
- [[Rust Regex]]
- [[wasm-bindgen]]
- [[rustfmt]]
- [[Rust io]]
- [[Rust rand]]
- [[Rust Prelude]]
- [[Rust tokio]]
- [[Rust Borrow Checker]]
- [[Rust Error Handling]]
# Guides
- [[Rust with WASM Guide]]
- [[Rust FileIO]]
# Rust Boilerplate
```rust
fn main(){
	println!("Hello World!");
}
```