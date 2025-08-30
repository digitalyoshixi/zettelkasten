---
tags:
  - programming
---
A program used to run a DLL file as if it were an executable from [[DLLMain]].
# Usage
### Running From Export name
```
rundll32.exe DLLName, ExportName arg1 arg2 ...
```
### Running from [[DLL Ordinal]]
```
rundll32.exe DLLName, #Ordinal
```