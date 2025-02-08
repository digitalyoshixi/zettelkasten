---
tags:
  - binary_exploitation
---
Byte data to be loaded into a program and executed as a [[Payload]].
-


# Injection Into A Code Cave
1. In a patching software like [[x64dbg]], allow somewhere to jump to a codecave
2. Add the instructions:
![[Shellcode-20250206151359138.webp]]
[[pushad]] and [[pushfd]]
3. Copy paste the hexidecimal data of your executable into the codecave
![[Shellcode-20250206151345078.webp]]
CTRL+E while selecting a codecave region
![[Shellcode-20250206151435376.webp]]
1. Afterwards, add the two instructions:
![[Shellcode-20250206151651182.webp]]
- [[popfd]]
- [[popad]]
