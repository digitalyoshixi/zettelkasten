---
tags:
  - reverse_engineering
  - debugging
---
1. Step past the point where the DLL is loaded in, keep stepping before the DLL is released. 
![[x64dbg Extract DLL-20240103010223393.webp]]
2. Locate the .dll in the Memory map
![[x64dbg Extract DLL-20240103010337568.webp]]
3. You can use [[Scylla]] to dump the DLL