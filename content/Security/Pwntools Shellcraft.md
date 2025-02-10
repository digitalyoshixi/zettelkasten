---
tags:
  - python
  - binary_exploitation
---
A module to create [[Shellcode]] for different architectures.

```python
import pwn
payload = pwn.shellcraft.i386.execve('/bin//sh')
```