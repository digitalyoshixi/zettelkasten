---
tags:
  - programming
  - win32api
  - windows
  - malware
  - security
---
# Code
```c
BOOL GetRemoteProcessHandle(IN LPWSTR szProcessName, OUT DWORD* dwProcessId, OUT OPTIONAL HANDLE* hProcess) 
{
	HANDLE			hSnapShot		= NULL;
	PROCESSENTRY32	ProcEntry		= { .dwSize = sizeof(PROCESSENTRY32) };

	// Initialize output parameters
	*dwProcessId = 0x00;
	if (hProcess) *hProcess = NULL;

	if ((hSnapShot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL)) == INVALID_HANDLE_VALUE) 
	{
		printf("[!] CreateToolhelp32Snapshot Failed With Error: %ld \n", GetLastError());
		goto _END_OF_FUNC;
	}

	if (!Process32First(hSnapShot, &ProcEntry)) 
	{
		printf("[!] Process32First Failed With Error: %ld \n", GetLastError());
		goto _END_OF_FUNC;
	}

	do 
	{
		if (lstrcmpiW(ProcEntry.szExeFile, szProcessName) == 0)
		{
			// Populate PID
			*dwProcessId = ProcEntry.th32ProcessID;

			// Populate Optional Process Handle
			if (hProcess) 
			{
				if ((*hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, ProcEntry.th32ProcessID)) == NULL)
				{
					printf("[!] OpenProcess Failed With Error: %ld \n", GetLastError());
				}
			}

			break;
		}

	} while (Process32Next(hSnapShot, &ProcEntry));


_END_OF_FUNC:
	if (hSnapShot != NULL)
		CloseHandle(hSnapShot);
	if (*dwProcessId == 0)	
		return FALSE;
	if (hProcess && *hProcess == NULL) // Process handle was requested but OpenProcess Failed 
		return FALSE;
	return TRUE;
}
```
# Example 2
- https://learn.microsoft.com/en-us/windows/win32/toolhelp/taking-a-snapshot-and-viewing-processes
# Explanation
1. Call [[CreateToolhelp32Snapshot]] to get the snapshot of processes currently running on the system
```c
// Takes a snapshot of the currently running processes 
hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

if (hSnapshot == INVALID_HANDLE_VALUE)
{
    printf("[!] CreateToolhelp32Snapshot Failed With Error: %lu\n", GetLastError());
    return FALSE;
}
```
2. [[Process32First]] is used to get the first process in the snapshot, [[Process32Next]] is used to get the next processes
3. Parse the [[PROCESSENTRY32]] fields
	1. `th32ProcessID` : PID
	2. `th32ParentProcessID` : PID of parent process
	3. `cntThreads` : # of threads
	4. `czExeFile` : executable filename associated with current process
4. [[OpenProcess()]] is used to open the process