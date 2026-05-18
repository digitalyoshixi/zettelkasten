---
tags:
  - blockchain
---
The first 4 bytes of a [[KECCAK-256]] hash of the signature of a function for [[Ethereum Bytecode|Ethereum Opcode]] file mapped to [[Application Binary Interface|ABI]].
```
Selector = Keccak-256(function signature)[0:4]
```