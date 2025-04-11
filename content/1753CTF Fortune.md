---
tags:
  - ctf
  - reverse_engineering
  - web
---
This site is using [[Web Assembly]]
![[1753CTF Fortune-20250411170233981.webp]]
Lets download this file:
![[1753CTF Fortune-20250411170607782.webp]]
https://fortune-ca29a1bd80cd.1753ctf.com/fortune_api.wasm
Lets disassemble this:
![[1753CTF Fortune-20250411170845109.webp]]
Then, decompile:
![[1753CTF Fortune-20250411171032989.webp]]
There is a flag verifying endpoint
![[1753CTF Fortune-20250411171632728.webp]]
![[1753CTF Fortune-20250411171648018.webp]]
I want to now debug the WASM code

1. Install wasmtime
2. `gdb --args wasmtime run -D debug-info -O opt-level=0 fortune_api.wasm`

This does not work, because this WASM file cannot run independent of the JS runtime it was built for.
So, we debug on the browser
![[1753CTF Fortune-20250411180908914.webp]]
The wasm instance is called fittingly, `instance`
![[1753CTF Fortune-20250411182513660.webp]]
So, if we want to memory dump, we can do:
```js
var mem = new Uint8Array(instance.exports.memory.buffer)
console.log(mem.slice(68640,68650))
```

Looking at the memory dump of 68640, we get this list: 
![[1753CTF Fortune-20250411183623966.webp]]
this just corresponds to this route: Not anything of note1
![[1753CTF Fortune-20250411183517075.webp]]

There is a function in the decompilation that is called `GetFlag`
![[1753CTF Fortune-20250411184048372.webp]]
It appears to be uncalled in the original wasm file:
![[1753CTF Fortune-20250411184322052.webp]]
Ok, makes sense, it simply sends a GET request to the backend for verification.

![[1753CTF Fortune-20250411184519462.webp]]