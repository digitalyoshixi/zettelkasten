---
tags:
  - programming
  - c
  - windows
---
Used open a URL from a given [[wininet]] connection.
```c
HINTERNET InternetOpenUrlW(
  [in] HINTERNET hInternet,       // Handle opened by InternetOpenW
  [in] LPCWSTR   lpszUrl,         // The file's URL
  [in] LPCWSTR   lpszHeaders,     // NULL
  [in] DWORD     dwHeadersLength, // 0x00
  [in] DWORD     dwFlags,         // INTERNET_FLAG_HYPERLINK | INTERNET_FLAG_IGNORE_CERT_DATE_INVALID | INTERNET_FLAG_IGNORE_CERT_CN_INVALID
  [in] DWORD_PTR dwContext        // 0x00
);
```
- `dwFlags` described in: https://learn.microsoft.com/en-us/windows/win32/api/wininet/nf-wininet-internetopenurlw