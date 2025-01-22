---
tags:
  - reverse_engineering
---
An address that can be referred to by a aliased name.
# Creation
`symbol = proj.loader.find_symbol("symbolname")`
# Symbol Linking Types
### Import Symbol
The function was not implemented in this program, this function must be imported from somewhere else.
They will not have an address associated with them
### Export Symbol
Function is implemented in the current program, and will have an address associated with it.
# Attributes
### symbol.owner
The [[angr Object]] that defines this symbol
### symbol.rebased_addr
The symbol's address in the global address space
### symbol.linked_addr
Address relative to the prelinked base of the binary
### symbol.relative_addr
Address relative to the object base. Equivalent to the [[Relative Virtual Addressing|RVA]]
### symbol.is_export
Boolean to see if the symbol is an export symbol
### symbol.is_import
Boolean to see if the symbol is an import symbol
### symbol.resovledby
If the symbol is import, then its address can be found with .resolvedby
![[angr Symbol-20240719011650307.webp]]