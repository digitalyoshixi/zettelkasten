---
tags:
  - security
  - reverse_engineering
---
A form of [[Binary Obfuscation]] that involves creating complex expressions that always evaluate to the same thing

```
if ((x*x + 1) % 5 == 3) { ... }  // Always false
```