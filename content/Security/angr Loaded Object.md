---
tags:
  - reverse_engineering
aliases:
  - angr Loaded BInary
---
A representation of loaded all linked [[angr Object]] mapped into a single memory space.
# Attributes
### proj.loader.all_objects
A list of all [[angr Object|angr BInary Objects]] loaded by the loader
![[angr Loaded Object-20240714201726364.webp]]
### proj.loader.main_object
The [[angr Object]] corresponding to the main program. Remember, when we load the object, we load all of its linked binaries aswell, so this main one is the non-linked binaries.
![[angr Loaded Object-20240714164738414.webp]]
### proj.loader.shared_objects
Dictionary mapping object names to the [[angr Object]].
![[angr Loaded Object-20240718213009724.webp]]
### proj.loader.all_elf_objects
Viewing all [[Executable and Linkable Format]] objects
![[angr Loaded Object-20240718213115238.webp]]
### proj.loader.all_pe_objects
Viewing all [[Portable Executable]] objects
![[angr Loaded Object-20240718213527669.webp]]
### proj.loader.extern_object
Viewing all external objects which are objects with unresolved imports and angr internals
### proj.loader.kernel_object
Providing addresses for emulated [[Syscall|Syscalls]]
### proj.loader.min_addr
Returns the minimum address that the program code is stored at
### proj.loader.max_addr
Returns the maximum address the program code occupies
# Methods
### proj.loader.find_object_containing()
Returns the binary which includes a given address
![[angr Loaded Object-20240714202101531.webp]]
### proj.loader.find_symbol()
Returns a [[angr Symbol]] object from the symbol name
![[angr Loaded Object-20240718220047256.webp]]