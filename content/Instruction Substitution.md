---
tags:
  - security
  - reverse_engineering
  - obscurity
  - malware
---
A form of [[Binary Obfuscation]] that involves replacing instructions with ones that are harder to evaluate.
```
mov eax, 0   ; becomes
xor eax, eax
```