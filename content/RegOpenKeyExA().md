---
tags:
  - programming
  - win32api
---
Used to get a handle to a [[Registry Key]].
```c
LSTATUS RegOpenKeyExA(
  [in]           HKEY   hKey, 		    // A handle to an open registry key
  [in, optional] LPCSTR lpSubKey, 	    // The name of the registry subkey to be opened (REGISTRY constant)
  [in]           DWORD  ulOptions, 	    // Specifies the option to apply when opening the key - Set to 0
  [in]           REGSAM samDesired, 	// Access Rights
  [out]          PHKEY  phkResult 	    // A pointer to a variable that receives a handle to the opened key
);
```