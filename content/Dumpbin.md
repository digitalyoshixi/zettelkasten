---
tags:
  - security
  - windows
---
A tool used to display information about [[Common Object File Format|COFF]].
- [[Dynamic Linked Library|DLL]] imports and exports
# Installation
1. Install [[Visual Studio]] and get C++ desktop development module
2. Add the directory `C:\Program Files\Microsoft Visual Studio\<Year>\<Edition>\VC\Tools\MSVC\<Version_Number>\bin\Hostx64\x64` to [[Windows PATH]]
# Dumping Exports
```
dumpbin /exports filename.dll
```
you can unobfuscate those names with [[undname]]
