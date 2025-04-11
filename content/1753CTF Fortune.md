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
