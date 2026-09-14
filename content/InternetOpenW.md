---
tags:
  - windows
  - programming
  - win32api
---
```c
HINTERNET InternetOpenW(
  [in] LPCWSTR lpszAgent,       // NULL
  [in] DWORD   dwAccessType,    // 0x00 (equivalent to INTERNET_OPEN_TYPE_PRECONFIG)
  [in] LPCWSTR lpszProxy,       // NULL
  [in] LPCWSTR lpszProxyBypass, // NULL
  [in] DWORD   dwFlags          // 0x00
);
```
Used to create a [[wininet]] session.
- Most parameters should be set to `NULL` or `0x00` unless you want to setup proxy configurations
# Usage
```c
// Opening the internet session handle, all arguments are NULL here since no proxy options are required
hInternet = InternetOpenW(NULL, 0x00, NULL, NULL, 0x00);
```