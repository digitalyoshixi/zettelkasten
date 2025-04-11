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