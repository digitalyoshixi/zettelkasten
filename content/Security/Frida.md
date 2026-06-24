---
tags:
  - reverse_engineering
---
A [[Software Instrumentation|Binary Instrumentation]] tool that can be used to hook and intercept function calls.
![[Frida-20260622232439551.webp]]
# Installation
### [[Windows]]
`pip install frida-tools`
The library is located at `<pythonfolder>/Lib/site-packages/frida-tools`
The example scripts are located at: `<pythonfolder>/Scripts/`
### [[Arch Linux|Arch]]
`sudo pacman -S python-frida python-frida-tools`
# Usage
### Run Binary
```
frida -f ./program -l instrumentation.js --stdio=inherit
```
```
frida PID -l instrumentation.js --stdio=inherit
```
### Trace Binary
```
frida-trace -f ./binary -i "CreateFile*" -I "KERNEL32.DLL"
```
- Trace binary for CreateFile calls from [[Kernel32]]
```
frida-trace PID -a "customLib.DLL!0x1234"
```
- Trace binary from PID at a custom function from module offset
# Concepts
- [[Frida Control Script]]
- [[Frida Instrumentation Script]]
- [[Frida Trace]]
- [[Frida Interceptor]]
- [[Frida Stalker]]
# Guides
- [[Frida Android]]
