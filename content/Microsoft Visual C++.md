---
tags:
  - windows
  - c
  - compilers
aliases:
  - msvc
  - msvc-redist
---
The microsoft [[C++]] compiler
# Installation (Via Build Tools)
- https://visualstudio.microsoft.com/downloads/
- Download Build Tools for Visual Studio 
# Usage
Open `x64 Native Tools Command Prompt For VS`
```
cl ./filename
```
### Creating a DLL
```
cl /LD ./filename.c user32.lib
```