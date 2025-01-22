---
tags:
  - reverse_engineering
---
These are single object files.
# Attributes
### obj.execstack
Returns a boolean if the object has an executable stack
![[angr Binary Object-20240714170309320.webp]]
### obj.pic
Returns a boolean if the object is [[Position Independent Executable|Position Independent Code]]
![[angr Binary Object-20240714170353073.webp]]
### obj.min_addr
Prints the lowest address occupied by this binary
### obj.max_addr
prints the largest address occupied by this binary
### obj.segments
prints all [[Executable and Linkable Format|ELF]] segments
![[angr Binary Object-20240715011037286.webp]]
### obj.sections
prints all [[Executable and Linkable Format|ELF]] sections
![[angr Binary Object-20240715011054023.webp]]
### obj.plt
An array of all defined function symbols
![[angr Binary Object-20240715024442133.webp]]
### obj.reverse_plt
a reverse mapping array of address -> function name
![[angr Binary Object-20240715024508981.webp]]
### obj.linked_base
Returns the prelinked base location if it exist
![[angr Binary Object-20240715025549864.webp]]
### obj.mapped_base
Returns the mapped base location if it exists
![[angr Binary Object-20240715025557478.webp]]
# Methods
### obj.find_segment_containing(addr)
Returns the segment that contains the given address
![[angr Binary Object-20240715024315023.webp]]
### obj.find_section_containing(addr)
Returns the section that contains a given address
![[angr Binary Object-20240715024339552.webp]]
