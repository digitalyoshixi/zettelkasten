---
tags:
  - security
  - windows
  - programming
aliases:
  - Loading DLL From Disk
---
Loading a DLL in the same process to store your malware payloads.
Custom code can be executed in two ways:
1. Making a DLL export for the code and calling it
2. Spawning a thread in [[DLLMain]] with the code
# Loading a DLL
```c
#include <Windows.h>
#include <Shlwapi.h> // For PathFindFileNameA
#include <stdio.h>

#pragma comment (lib, "Shlwapi.lib")


int main(int argc, char* argv[]) 
{
	if (argc < 2)
	{
		printf("[!] Missing Parameter. Usage: \"%s\" <Dll Payload Path> \n", PathFindFileNameA(argv[0]));
		return -1;
	}

	printf("[i] Injecting \"%s\" Into The Local Process Of Pid: %d \n", PathFindFileNameA(argv[1]), GetCurrentProcessId());

	printf("[i] Loading Dll ... ");

	if (LoadLibraryA(argv[1]) == NULL) 
	{
		printf("\n[!] LoadLibraryA Failed With Error: %lu \n", GetLastError());
		return -1;
	}

	printf("[+] DONE \n");

	printf("[#] Press <Enter> To Quit ... ");
	getchar();

	return 0;
}
```