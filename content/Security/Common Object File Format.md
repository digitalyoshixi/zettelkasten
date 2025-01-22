---
tags:
  - malware
aliases:
  - COFF
---
For Microsoft systems.
Worse version of the [[Executable and Linkable Format|ELF]] format
# Format
https://wiki.osdev.org/COFF

| Structure                 | Purpose                                                                                                               | Location                                                                                                           | Length                                                                                                                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| File Header               | Stores the basic information about the file as well as pointers to the other structures.                              | At the beginning of the file, except in Microsoft PE/COFF Image files (see above).                                 | Fixed structure length.                                                                                                     |
| Optional Header           | Stores additional information about the execution of the file.                                                        | Only present if indicated by the File Header. Immediately follows the File Header.                                 | Specified in the File Header                                                                                                |
| Section Header            | Stores information about the different sections defined in the file.                                                  | Immediately following the Optional Header. If no Optional Header is provided, immediately follows the File Header. | Calculated by the number of sections (specified in the File Header) multiplied by the fixed structure length.               |
| Section Relocation Table  | Allows the file to be relocated to any area of memory by providing information on which addresses need to be changed. | At most one table exists for each Section. Location is indicated by the corresponding Section Header.              | Calculated by the number of relocation entries (specified in the Section header) multiplied by the fixed structure length.  |
| Section Line Number Table | Provides debugging information to map code addresses to source file line numbers.                                     | At most one table exists for each Section. Location is indicated by the corresponding Section Header.              | Calculated by the number of line number entries (specified in the Section header) multiplied by the fixed structure length. |
| Symbol Table              | Stores information on each symbol defined or declared by the code.                                                    | Indicated to a pointer in the File Header.                                                                         | Calculated by the number of symbols (specified in the File Header) multiplied by the fixed structure length.                |
| String Table              | Stores any Section or Symbol names that are longer than eight characters.                                             | Immediately following the Symbol table.                                                                            | Indicated by the first 32 bits of the string table, evaluated as a long                                                     |