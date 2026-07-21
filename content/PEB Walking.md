---
tags:
  - security
---
A technique to resolve a module address at runtime in a [[Address Space Layout Randomization|ASLR]] environment.
![[PEB Walking-20260721140538291.webp]]
1. Find [[Process Environment Block|PEB]] ([[Getting PEB Address]])
2. Get key offset `0x18` of PEB to get the [[PEB_LDR_DATA]] data structure
3. Get InMemoryOrderModuleList from the PEB_LDR_DATA 
4. Traverse the module list with flinks to get [[LDR_DATA_TABLE_ENTRY]] module data structure
5. Find matched function signature
