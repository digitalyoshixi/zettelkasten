---
tags:
  - malware
  - PE
---
Juicy lump of delectable lard~!
![[Optional Header-20240331010017048.webp]]
# Members
### Magic
![[Optional Header-20240331010035544.webp]]
Tells us if its either PE32 or PE32+ <- which is PE64
### Size Of Code
Tells us size of .text section inside the [[Section Table]]
### AddressOfEntryPoint
Tells us the starting address at which the executable starts execution from
### Subsystem
![[Optional Header-20240331010222218.webp]]
Tells us if its a GUI application or console app
# ImageDataDirectory
Lookup table for all the addresses of all data directories within the [[Section Table]]
![[Optional Header-20240331010839987.webp]]

