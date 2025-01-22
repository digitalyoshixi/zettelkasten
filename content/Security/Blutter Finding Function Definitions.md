---
tags:
  - flutter
  - reverse_engineering
---
You should first `cat pp.txt | grep <someknownstring>` to see where the address of a known string is located.
![[Blutter Finding Function Definitions-20240831202237028.webp]]
Once you know the address, you can 
`grep -ri 0x28946c /asm` to see which assembly file(s) includes this address.