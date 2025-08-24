---
tags:
  - security
  - reverse_engineering
  - malware
aliases:
  - Trampoline Obfuscation
---
Obfuscating [[Import Address Table|IAT]],
Instead of calling from IAT directly, we call a [[Trampoline Code|Trampoline]] that computes a [[C Function Pointers|FP]] to the function we want to call.