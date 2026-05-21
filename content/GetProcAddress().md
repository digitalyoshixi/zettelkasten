---
tags:
  - windows
  - win32api
---
A [[Win32 API]] function to get the address of a function in a [[Dynamic Linked Library|DLL]].
```
FARPROC GetProcAddress(
  [in] HMODULE hModule,
  [in] LPCSTR  lpProcName
);
```
- `hModule` can be gotten from [[GetModuleHandle()]]
- `lpProcName` is the string name of the function