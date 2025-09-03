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
- [[Rustc]]
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
- [[Rust Panic]]
- [[Rust Enums]]
- [[Rust Expect]]
- [[Rust ?]]
- [[Rust Iterators]]
- [[Rust Allow Unused Variables]]
- [[Rust Strings]]
- [[Rust Regex]]
- [[Rustup]]
- [[Cargo]]
- [[wasm-bindgen]]
- [[rustfmt]]
- [[Rust io]]
- [[Rust Prelude]]
# Guides
- [[Rust with WASM Guide]]
- [[Rust FileIO]]
# Rust Boilerplate
```rust
fn main(){
	println!("Hello World!");
}
```