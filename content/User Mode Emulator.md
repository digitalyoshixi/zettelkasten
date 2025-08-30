---
tags:
  - virtualization
  - os
---
A [[Emulation|Emulator]] that:
- Emulates [[CPU Emulator]]
- Emulates [[Dynamic Linked Library|DLL Exports]] OR [[Syscall]]
- Emulates processes
All user-mode emulators use [[Unicorn]] beneath the hood.
# Implementations
- [[Speakeasy]]
- [[Qiling]]
- [[Dumpulator]]
# Emulation Scope
### DLL Export Emulation
![[User Mode Emulator-20250830174705432.webp]]
### Syscall Emulation
![[User Mode Emulator-20250830174727353.webp]]