---
tags:
  - security
  - windows
  - win32api
---
Used to read the contents after a URL is opened in [[wininet]].
```c
BOOL InternetReadFile(
  [in]  HINTERNET hFile,                  // Handle opened by InternetOpenUrlW
  [out] LPVOID    lpBuffer,               // Buffer to store the payload
  [in]  DWORD     dwNumberOfBytesToRead,  // The number of bytes to read
  [out] LPDWORD   lpdwNumberOfBytesRead   // Pointer to a variable that receives the number of bytes read
);
```
# Usage
```c
pFileBuffer = (PBYTE)LocalAlloc(LPTR, 272);
InternetReadFile(hInternetFile, pFileBuffer, 272, &dwTmpBytesRead);
```