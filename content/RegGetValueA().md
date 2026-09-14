---
tags:
  - windows
  - programming
  - security
---
Function to read the value of a registry key.
- You should call it once with `NULL` as the destination to get the payload size, then allocate the buffer and read again
```c
LSTATUS RegGetValueA(
  [in]                HKEY    hkey,     // A handle to an open registry key
  [in, optional]      LPCSTR  lpSubKey, // The path of a registry key relative to the key specified by the hkey parameter
  [in, optional]      LPCSTR  lpValue,  // The name of the registry value
  [in, optional]      DWORD   dwFlags,  // The flags that restrict the data type of value to be queried
  [out, optional]     LPDWORD pdwType,  // A pointer to a variable that receives a code indicating the type of data stored in the specified value
  [out, optional]     PVOID   pvData,   // A pointer to a buffer that receives the value's data
  [in, out, optional] LPDWORD pcbData   // A pointer to a variable that specifies the size of the buffer pointed to by the pvData parameter, in bytes
);
```
- `dwFlags` can be used to restrict the data type