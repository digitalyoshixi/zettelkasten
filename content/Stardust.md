---
tags:
  - security
aliases:
  - Modern Position Independent Implant
---
A [[C2 Implant]] template written to be customizable and [[Position Independent Executable|PIE]].
- Support for global variables
- Support for raw strings
- Support for compile-time hashing
# Design
Implant is built with following sections:
```
[   .text$A    ] aligns the stack, executes entrypoint, util function to get the base address, etc. 
[   .text$B    ] C entrypoint, implant prepation, communication, commands, evasion techniques, etc.
[   .rdata*    ] literal strings and data (maybe even configuration) 
[  page align  ] alignt page by 0x1000 so ".global" section is in its own page
[   .global    ] global variables
[   .text$E    ] code to get the rip of the end of implant
```
