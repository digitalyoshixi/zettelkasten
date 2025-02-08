---
tags:
  - binary_exploitation
---
# Injection Into A Code Cave
1. In a patching software like [[x64dbg]], allow somewhere to jump to a codecave
2. Add the instructions:
![[Shellcode-20250206151359138.webp]]
[[pushad]] and [[pushfd]]
1. Copy paste the hexidecimal data of your executable into the codecave
![[Shellcode-20250206151345078.webp]]
CTRL+E while selecting a codecave region
![[Shellcode-20250206151435376.webp]]
2. Afterwards, add the two instructions:
![[Shellcode-20250206151651182.webp]]
- [[popfd]]
- [[popad]]