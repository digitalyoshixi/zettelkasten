---
tags:
  - python
  - binary_exploitation
---
A module to create [[Shellcode]] for different architectures.
# Shell
```python
import pwn
payload = pwn.shellcraft.i386.execve('/bin//sh')
```
# Cat Flag
```python
import pwn
payload = pwn.shellcraft.i386.execve('/bin//sh')
```