---
tags:
  - web
aliases:
  - WASM
---
A 32-bit [[Instruction Set Architecture|ISA]] with a set of [[Bytecode]] designed for a [[Stack-Based Virtual Machine]].
We can migrating low level software written in [[Rust]], [[C]], [[COBOL]] in a web browser at near native performance.
It consists of web assembly [[Bytecode]] compiled to WASM binary.
# Creating WASM Binaries
1. Use [[Web Assembly Text]]
2. Use [[Emscripten]] to convert C/C++ program to [[WASM Module]]
3. Use [[AssemblyScript]] to convert [[TypeScript]] into [[WASM Module]]
# WASM In the Browser
![[Web Assembly-20250831123806105.webp]]
- WASM must be instantiated by a javascript handler, as it cannot talk to the [[Document Object Model|DOM]] directly.
# Boilerplates
### JS Handler
```js
// providing functions for WASM to callback
let imports = {
	math : {
		callback : x => console.log("result is", x);
	}
}
let module = await WebAssembly.instantiateStreaming(fetch('main.wasm'), imports)
// using exports of WASM
let x = module.instance.exports.add(5,10)
```
### WAT
```js
(module
	(import "math" "callback" (func $callback))	
	(export "add" (func $add))
	(export "subtract" (func $subtract))
	(func $add (param $a i32) (param $b i32) (result i32)
		local.get $a
		local.get $b
		i32.add
		local.set $sum ;; set result to sum
		local.get $sum ;; put sum onto stack
		call $callback ;; call callback with $sum
		local.get $sum ;; put sum onto stack again
	)
	(func $subtract (param $a i32) (param $b i32) (result i32)
		local.get $a
		local.get $b
		i32.sub
	)
)
```
# Compiling [[Web Assembly Text|WAT]]
```
wat2wasm myfile.wat
```
# Concepts
- [[WASM Module]]
- [[Web Assembly Text]]
	- [[WASM Program with S-Expr]]
- [[Web Assembly System Interface]]
- [[Web Assembly Binary Toolkit]]
- [[WASM Runtime]]
	- [[wasmtime]]
- [[ASMjs]]
# Guides
- https://rsms.me/wasm-intro
- https://invidious.yoshixi.net/watch?v=3sU557ZKjUs&listen=false
- https://invidious.yoshixi.net/watch?v=VGLnqkegX-g&listen=false
- https://webassembly.github.io/spec/
- https://developer.mozilla.org/en-US/docs/WebAssembly