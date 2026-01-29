---
tags:
  - linux
  - reverse_engineering
---
Includes all information required at [[Linker|Link Time]] for linking the target object file to build a working executable.

# Sections List
each section is a [[ELF32_Shdr]] 
- **.text**: code
- **.data**: initialized global data
- **.rodata**: initialized read-only data for [[C Macro|C Constants]]
- **.bss**: uninitialized global data
- **.plt**: procedure linkage table ([[Import Address Table|IAT]] equivalent)
- **.got**: GOT entries dedicated to dynamically linked global variables
- **.got.plt**: got entries dedicated to dynamically linked fuctions
- **.symtab**: global symbol table
- **.dynamic**: holds all needed information for dynamic linking
- **.dynsym**: symbol tables dedicated to dynamically linked symbols
- **.strtab**: string table of the .symtab section
- **.dynstr**: string table of .dynsym section.
- **.interp**: RTLD embedded string.
- **.rel.dyn**: global variable relocation table.
- **.rel.plt**: function relocation table.