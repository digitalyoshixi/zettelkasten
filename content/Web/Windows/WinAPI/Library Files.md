---
tags:
  - windows
  - win32api
aliases:
  - .lib
  - Static Libraries
  - Import Libraries
---
A library is an archive of already compiled code.
They can be 2 things:
1. Static Libraries - Libraries that contain object files
2. Import Libraries - Libraries that contain symbols to allow linker to link with a [[Dynamic Linked Library|DLL]]
### Static libraries
They are like header files, but they include the binary, not the text. 
### Import Libraries
Used by the [[Linker]] to help find DLL files and provide debug information.
