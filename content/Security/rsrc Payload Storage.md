---
tags:
  - security
aliases:
  - .rsrc Payload Storage
---
Storing payload data in the [[.rsrc]] section of a program.
- `R` read only section, must memcpy to a different region to edit it
# Process
1. Add a resource file in VSCode:
2. ![[rsrc Payload Storage-20260729143345871.webp]]
3. ![[rsrc Payload Storage-20260729143416045.webp]]
4. Add a new resource to the new resource section:
   ![[rsrc Payload Storage-20260729143724819.webp]]
5. Import an .ico file:
   ![[rsrc Payload Storage-20260729143745733.webp]]
6. Select your payload ico file
   ![[rsrc Payload Storage-20260729143843744.webp]]
7. Set the resource type to RCDATA
   ![[rsrc Payload Storage-20260729143859704.webp]]
8. The generated resource.h file should have the resource identifier noted in the `#define`
   ![[rsrc Payload Storage-20260729144002750.webp]]
You can use this resource using [[Win32 API]]:
```c
#include <Windows.h>
#include <stdio.h>
#include "resource.h"

int main() {
	HGLOBAL		hGlobal                 = NULL;
	PVOID		pPayloadAddress         = NULL;
	SIZE_T		sPayloadSize            = NULL;

	// Get the location to the data stored in .rsrc by its id *IDR_RCDATA1*
	hRsrc = FindResourceW(NULL, MAKEINTRESOURCEW(IDR_RCDATA1), RT_RCDATA);
	if (hRsrc == NULL) {
		// in case of function failure 
		printf("[!] FindResourceW Failed With Error : %d \n", GetLastError());
		return -1;
	}

	// Get HGLOBAL, or the handle of the specified resource data since its required to call LockResource later
	hGlobal = LoadResource(NULL, hRsrc);
	if (hGlobal == NULL) {
		// in case of function failure 
		printf("[!] LoadResource Failed With Error : %d \n", GetLastError());
		return -1;
	}

	// Get the address of our payload in .rsrc section
	pPayloadAddress = LockResource(hGlobal);
	if (pPayloadAddress == NULL) {
		// in case of function failure 
		printf("[!] LockResource Failed With Error : %d \n", GetLastError());
		return -1;
	}

	// Get the size of our payload in .rsrc section
	sPayloadSize = SizeofResource(NULL, hRsrc);
	if (sPayloadSize == NULL) {
		// in case of function failure 
		printf("[!] SizeofResource Failed With Error : %d \n", GetLastError());
		return -1;
	}
	
	// Printing pointer and size to the screen
	printf("[i] pPayloadAddress var : 0x%p \n", pPayloadAddress);
	printf("[i] sPayloadSize var : %ld \n", sPayloadSize);
	printf("[#] Press <Enter> To Quit ...");
	getchar();
	return 0;
}
```