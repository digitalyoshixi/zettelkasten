---
tags:
  - programming
  - windows
  - win32api
---
A [[Win32 API]] function used to get a [[Handle]].
```c
HMODULE GetModuleHandleA(
  [in, optional] LPCSTR lpModuleName
);
```
Can be used to get the handle of a [[Dynamic Linked Library|DLL]] loaded into memory already
```c
HMODULE hModule = GetModuleHandleA("sampleDLL.dll");
```