---
tags:
  - security
---
Attacks that move [[rsp]] to a different memory address.
- Can be used to evade [[Control Flow Enforcement Technology|CET]] for [[Backwards ROP]]
# ROP Stack Pivot
https://ir0nstone.gitbook.io/notes/binexp/stack/stack-pivoting
We can change rsp with:
### pop rsp

### xchg \<reg\>, rsp
```
pop <reg>                <=== return pointer
<reg value>
xchg <reg>, rsp
```
### leave; ret
This instruction can overwrite rbp

# Heap Stack Pivot
Creating a fake [[OS Stack|Stack]] on the [[Heap]] by making [[rsp|esp]] point to that heap location.
![[Stack Pivot-20260112042625699.webp]]