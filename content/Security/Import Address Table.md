---
tags:
  - malware
  - PE
aliases:
  - IAT
---
Array of all function/API [[Relative Virtual Addressing]]. 
# Table of Addresses
It stores only addresses. Addresses of all functions you need in your program.
If you get a function from a win32 DLL like CreateThread, that will show up in the IAT
![[Import Address Table-20240331012342666.webp]]
And when its to be called, the address is referenced
# IAT Write Protection
If an attacker rewrites the IAT to point to their malicious DLL, well, youre fucked!
That's why its write protected