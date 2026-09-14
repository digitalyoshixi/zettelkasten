---
tags:
  - programming
  - win32api
  - windows
  - c
---
Used to set the value of a registry key opened with [[RegOpenKeyExA()]]
```c
LSTATUS RegSetValueExA(
  [in]           HKEY       hKey,            // A handle to an open registry key
  [in, optional] LPCSTR     lpValueName,     // The name of the value to be set
                 DWORD      Reserved,        // Set to 0
  [in]           DWORD      dwType,          // The type of data pointed to by the lpData parameter
  [in]           const BYTE *lpData,         // The data to be stored
  [in]           DWORD      cbData           // The size of the information pointed to by the lpData parameter, in bytes
);
```
- 