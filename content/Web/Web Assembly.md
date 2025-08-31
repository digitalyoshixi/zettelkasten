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
2. Use [[Emscripten]] to convert C/C++ program to WASM
3. Use [[AssemblyScript]] to convert [[TypeScript]] into WASM
# Guides
- https://rsms.me/wasm-intro
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
# Concepts
- [[WASM Module]]
- [[Web Assembly Text]]