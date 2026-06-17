---
tags:
  - programming
  - c
aliases:
  - bcrypt.h
---
# Performing [[Advanced Encryption Standard|AES]] encryption
```c

typedef struct _AES {
	PBYTE	pPlainText;         // base address of the plain text data 
	DWORD	dwPlainSize;        // size of the plain text data
	PBYTE	pCipherText;        // base address of the encrypted data	
	DWORD	dwCipherSize;       // size of it (this can change from dwPlainSize in case there was padding)
	PBYTE	pKey;               // the 32 byte key
	PBYTE	pIv;                // the 16 byte iv
} AES, *PAES;


// Wrapper function for InstallAesEncryption that makes things easier
BOOL SimpleEncryption(IN PVOID pPlainTextData, IN DWORD sPlainTextSize, IN PBYTE pKey, IN PBYTE pIv, OUT PVOID* pCipherTextData, OUT DWORD* sCipherTextSize) {

	if (pPlainTextData == NULL || sPlainTextSize == NULL || pKey == NULL || pIv == NULL)
		return FALSE;
	
	// Intializing the struct
	AES Aes = {
		.pKey        = pKey,
		.pIv         = pIv,
		.pPlainText  = pPlainTextData,
		.dwPlainSize = sPlainTextSize
	};

	if (!InstallAesEncryption(&Aes)) {
		return FALSE;
	}

	// Saving output
	*pCipherTextData = Aes.pCipherText;
	*sCipherTextSize = Aes.dwCipherSize;

	return TRUE;
}


// Wrapper function for InstallAesDecryption that make things easier
BOOL SimpleDecryption(IN PVOID pCipherTextData, IN DWORD sCipherTextSize, IN PBYTE pKey, IN PBYTE pIv, OUT PVOID* pPlainTextData, OUT DWORD* sPlainTextSize) {

	if (pCipherTextData == NULL || sCipherTextSize == NULL || pKey == NULL || pIv == NULL)
		return FALSE;

	// Intializing the struct
	AES Aes = {
		.pKey          = pKey,
		.pIv           = pIv,
		.pCipherText   = pCipherTextData,
		.dwCipherSize  = sCipherTextSize
	};

	if (!InstallAesDecryption(&Aes)) {
		return FALSE;
	}

	// Saving output
	*pPlainTextData = Aes.pPlainText;
	*sPlainTextSize = Aes.dwPlainSize;

	return TRUE;
}


```