---
tags:
  - security
  - reverse_engineering
  - obscurity
  - malware
---
A form of [[Binary Obfuscation]] that involves injecting code into a running [[Process Control Thread|Thread]] to hide execution flow.
# Classic Pattern
1. [[VirtualAlloc]]
2. [[VirtualProtect]]
3. [[GetThreadContext]]
4. [[SetThreadContxt]]