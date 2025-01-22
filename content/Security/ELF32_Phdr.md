---
tags:
  - os
  - linux
---
![[ELF32_Phdr-20240715010740630.webp]]
# Fields
- p_type: Segment type
- p_flags: Segment attributes
- p_offset: File offset of segment
- p_vaddr: Virtual address of segment
- p_paddr: Physical address of segment
- p_filesz: Size of segment on disk
- p_memsz: Size of segment in memory
- P_align: segment alignment in memory
### p_type (Segment Types)
The most common segment types include:
- PT_NULL: unassigned segment (usually first entry of Program Header Table).
- PT_LOAD: Loadable segment.
- PT_INTERP: Segment holding .interp section.
- PT_TLS: Thread Local Storage segment (Common in statically linked binaries).
- PT_DYNAMIC: Holding .dynamic section.