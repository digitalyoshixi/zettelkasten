---
tags:
  - programming
  - llvm
  - wasm
---
A [[Compiler Backend]] for converting [[C++|CPP]], [[Rust]], [[Web Assembly Text|WAT]] to [[WASM Module]]
It is a fork of [[Low Level Virtual Machine|LLVM]].
# Installation
```
yay -S emscripten
source /etc/profile.d/emscripten.sh
```
# Usage
```
emcc hello.c -o index.html
```