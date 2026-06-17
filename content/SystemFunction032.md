---
tags:
  - windows
aliases:
  - NTAPI RC4
  - SystemFunction033
---
A small implementation of [[Rivest Cipher 4|RC4]] function.
```c
 NTSTATUS SystemFunction032
 (
  struct ustring*       data,
  const struct ustring* key
 )
```

```c
typedef struct
{
	DWORD	Length;         // Size of the data to encrypt/decrypt
	DWORD	MaximumLength;  // Max size of the data to encrypt/decrypt, although often its the same as Length (USTRING.Length = USTRING.MaximumLength = X)
	PVOID	Buffer;         // The base address of the data to encrypt/decrypt

} USTRING;

```

# Usage
```c
typedef struct
{
	DWORD	Length;
	DWORD	MaximumLength;
	PVOID	Buffer;

} USTRING;

typedef NTSTATUS(NTAPI* fnSystemFunction032)(
	struct USTRING* Data,
	struct USTRING* Key
);

/*
Helper function that calls SystemFunction032
* pRc4Key - The RC4 key use to encrypt/decrypt
* pPayloadData - The base address of the buffer to encrypt/decrypt
* dwRc4KeySize - Size of pRc4key (Param 1)
* sPayloadSize - Size of pPayloadData (Param 2)
*/
BOOL Rc4EncryptionViaSystemFunc032(IN PBYTE pRc4Key, IN PBYTE pPayloadData, IN DWORD dwRc4KeySize, IN DWORD sPayloadSize) {

	NTSTATUS STATUS	= NULL;
	
	USTRING Data = { 
		.Buffer         = pPayloadData,
		.Length         = sPayloadSize,
		.MaximumLength  = sPayloadSize
	};

	USTRING	Key = {
		.Buffer         = pRc4Key,
		.Length         = dwRc4KeySize,
		.MaximumLength  = dwRc4KeySize
	};

	fnSystemFunction032 SystemFunction032 = (fnSystemFunction032)GetProcAddress(LoadLibraryA("Advapi32"), "SystemFunction032");

	if ((STATUS = SystemFunction032(&Data, &Key)) != 0x0) {
		printf("[!] SystemFunction032 FAILED With Error: 0x%0.8X \n", STATUS);
		return FALSE;
	}

	return TRUE;
}
```

# SystemFunction033
```c

typedef struct
{
	DWORD	Length;
	DWORD	MaximumLength;
	PVOID	Buffer;

} USTRING;


typedef NTSTATUS(NTAPI* fnSystemFunction033)(
	struct USTRING* Data,
	struct USTRING* Key
	);


/*
Helper function that calls SystemFunction033
* pRc4Key - The RC4 key use to encrypt/decrypt
* pPayloadData - The base address of the buffer to encrypt/decrypt
* dwRc4KeySize - Size of pRc4key (Param 1)
* sPayloadSize - Size of pPayloadData (Param 2)
*/
BOOL Rc4EncryptionViSystemFunc033(IN PBYTE pRc4Key, IN PBYTE pPayloadData, IN DWORD dwRc4KeySize, IN DWORD sPayloadSize) {

	NTSTATUS	STATUS = NULL;

	USTRING		Key = { 
			.Buffer        = pRc4Key, 
			.Length        = dwRc4KeySize,
			.MaximumLength = dwRc4KeySize 
	};
		
	USTRING 	Data = {
			.Buffer         = pPayloadData, 	
			.Length         = sPayloadSize,		
			.MaximumLength  = sPayloadSize 
	};

	fnSystemFunction033 SystemFunction033 = (fnSystemFunction033)GetProcAddress(LoadLibraryA("Advapi32"), "SystemFunction033");

	if ((STATUS = SystemFunction033(&Data, &Key)) != 0x0) {
		printf("[!] SystemFunction033 FAILED With Error: 0x%0.8X \n", STATUS);
		return FALSE;
	}

	return TRUE;
}
```