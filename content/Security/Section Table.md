---
tags:
  - malware
  - PE
---
### Section table: 
Contains a table of sections that it routes you to. This includes:
- [[Executable Sections]](.text, CODE)    
- [[Data Section]] (.data, DATA)
- [[RData Section]] (.rdata)
- [[BSSData Section]] (.bss)
- [[Export Directory Section|EDT]](.edata)
- [[Import Directory Table|IDT]] (.idata)
- [[Resource Directory Table]](.rsrc)
- [[Exception Directory Table]]
- [[Security Directory Table]]
- [[Base Relocation Table]] (.reloc)
- [[Debug Directory Table]](.debug)
- [[TLS Directory Table]]
- [[Bound Imports]]
- [[Import Address Table|IAT]]
##### Section Headers
Every section whether it be .idata, .text, .bss , they have their own section header.
![[Section Table-20240331014017503.webp|483]]
Name - Name of section
Physical Address - Where it is in memory
Virtual Size - Size of section
##### Minimum Viable Product
The smallest PE file can have at least 2 sections:
- .data
- .text
each section must follow [[Data Alignment]]
# PE Tables
- [[Import Lookup Table|INT]]
- [[Hint & Name Table]]