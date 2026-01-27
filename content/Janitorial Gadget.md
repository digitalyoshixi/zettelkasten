---
tags:
  - security
---
A [[ROP Gadget]] that exists to unbreak your top chain.
# Examples
```
pop r12
pop rdi
pop rsi
ret
```

```
add rsp, 0x40
ret
```