---
tags:
  - programming
  - x86
  - assembly
aliases:
  - x86 scasb
  - x86 scasw
  - x86 scasd
---
```
rep scasb
```
A instruction to be repeated with [[x86 rep]] used to search for occurances of `al` starting from destination address stored in `esi` up to a max length dictated by `ecx`