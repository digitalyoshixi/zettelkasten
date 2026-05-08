---
tags:
  - security
aliases:
  - BOF
---
A small compiled [[Common Object File Format|COFF]] object used as part of a [[Command and Control Server|C2]] to be dyamically loaded and executed within the agent's process memory. Introduced in [[Cobalt Strike]] to allow functionality without recompiling.

Can be used for:
- [[Process Injection]]
- [[Reflective Code Loading]]
# Structure
```
void go(char *args, unsigned long length);
```
- No [[Standard Library]]
- No static initializers (globals, static, etc)
- Minimal imports
- Direct API interaction with any given libraries (`beacon.h`)