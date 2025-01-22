---
tags:
  - os
---
Ensures nothing else but trusted firmware/software signed with a digital signature can execute during boot.
Created to prevent [[Rootkit|Rootkits]] and [[Virus|Viruses]]
### Signed Software
A software is trustworthy if they have a digital signature.
`bootmgr.efi` has a signature like this:
![[Secure Boot-20240525143410534.webp]]
These signatures can be manually approved