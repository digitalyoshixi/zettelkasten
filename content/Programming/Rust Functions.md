---
tags:
  - rust
---
# Imperative
### Void Return Function
```rust
fn greet(){
	println!("hello world");
}
```
### Returning Function
##### Explicit Return
```rust
fn diceroll() -> i32 {
	return 4;
}
```
##### Return Tail
```rust
fn diceroll() -> i32 {
	4
}
```
# FP
### Generic Function
```rust
fn foobar<T>(arg : T) {
	println!(arg);
}
```
or
```rust
fn foobar<L, R>(left : L, right : R) {
	println!(L);
	println!(R);
}
```