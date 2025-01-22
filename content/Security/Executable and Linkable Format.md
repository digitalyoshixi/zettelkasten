---
tags:
  - linux
aliases:
  - ELF
---
Format for linux executables
# Anatomy
### Elf Header
Contains generatl information about the binary.
- e_indent: Array of 16 bytes containing identification flags about the file
	- El_MAG0-3: ELF [[Magic Numbers]]
	- El_CLASS: File class
	- El_DATA: File's data encoding/encryption
	- El-VERSION: File's version
	- El_OSABI: [[Operating System|OS]]/[[Application Binary Interface|ABI]] identification
	- El_ABIVERSION [[Application Binary Interface|ABI]] version
	- El_PAD: Start of padding bytes
	- El_NIDENT: size of ei_ident
- e_type: Type of executable
- e_machine: File's architecture
- e_version: Object file version
- e_entry: Entry point of application
- e_phoff: File offset of the Program Header Table
- e_shoff: File offset of Section Header Table
- e_flags: Processor-specific flags associated with the file
- e_ehsize: ELF header size
- e_phentsize: Program Header entry size in the Program Header Table
- e_phnum: Number of Program Headers
- e_shentsize: Section Header entry size in Section Header Table
- e_shnum: Number of Section headers
- e_shstrndx: Index in the Section Header Table Denoting Section dedicated to Hold Section names
### Sections
Includes all information required at linktime for linking the target object file to build a working executable.
Needed on linktime, but irrelevant on runtime.
each section is a [[ELF32_Shdr]] 
Sections include:
- **.text**: code
- **.data**: initialized data
- **.rodata**: initialized read-only data
- **.bss**: uninitialized data
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
### Segments/Program headers
These break down the ELF binary into chunks to be executed. Not needed at linktime but required at runtime
Each segment is a [[ELF32_Phdr]] structure
# Elf Reading Tools
- [[binutils]]