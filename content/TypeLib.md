---
tags:
  - windows
  - security
  - malware
---
A file use by a [[Component Object Model|COM]] that stores metadata, and interface definitions.
Stored as a `.tlb` file
![[TypeLib-20260522140625604.webp]]
# COM Linkage
Typelibs are linked to [[Component Object Model|COM]] by [[Registry Key]] of [[CLSID]]'s hive.
![[TypeLib-20260522142929282.webp]]
```
# Typelib Location
HKLM\Software\Classes\TypeLib\<TypeLib ID>\<Version>
# CLSID Location
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\TypeLib\{0D452EE1-E08F-101A-852E-02608C4D0BB4}\2.0i
```