---
tags:
  - malware
  - reverse_engineering
  - PE
aliases:
  - PE
---
# Table Of Contents
```table-of-contents
```
# PE
Bastardized version of the [[Common Object File Format|COFF]] format
The standard file format for exe,dll,sys,src files
Portable on all windows OS and all cpus.
PE files loaded onto the disc are the exact same format as it would be when loaded into memory
# Good At:
- Holds 90% of information about a malware
	- Import Tables
- Bypasses [[Packing]]
# Structure
Unlike COM-type executables *(where execution starts at the first byte)*, 
PE file format to tell us where exactly we start.
### Image
![[Portable Executable-20240318014946865.webp|416]]
- [[DOS MZ header]]
- [[DOS stub]]
- [[Rich Header]]
- [[NT Header]]
	- [[PE Signature]]
	- [[File Header]]
	- [[Optional Header]]
- [[Section Table]]

