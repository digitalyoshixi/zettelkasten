---
tags:
  - malware
  - PE
aliases:
  - Import Name Table
  - ILT
  - INT
---
### Import lookup table/Import Name Table (ILT/INT)
The important part of the import lookup table are the imported DLL name and the 2 pointers that point to the 2 copies of the array: “IMAGE_IMPORT_BY_NAME” they are:
1. Characteristics
2. FirstThunk
    

The 2 arrays terminate at a null terminator and also run concurrently/parallel to each other.

The question is, why is there 2 pointers & 2 arrays that run paralell and point to the same thing? What the piss is the point of this?

The reason is, Characteristics pointer & array are unmodified. Sometimes called the hint-name table.

The array pointed to by FirstThunk is overwritten by the PE loader. The loader iterates each pointer in the array and replaces them with the address of the function the pointer points to.

This [[FirstThunk]] Array is now an RVA the IAT table

ILT consists of an array of 32-bit numbers (for PE32) or 64-bit numbers for (PE32+), the last one is zeroed-out to indicate the end of the ILT

- **Bit 31/63 (most significant bit)**: Ordinal/Name flag, it specifies whether to import the function by name or by ordinal.
    

- **Bits 15-0:** If the Ordinal/Name flag is set to `1` these bits are used to hold the 16-bit ordinal number that will be used to import the function, bits 30-15/62-15 for PE32/PE32+ must be set to `0`.
    
- **Bits 30-0:** If the Ordinal/Name flag is set to `0` these bits are used to hold an RVA of a Hint/Name table.
    



