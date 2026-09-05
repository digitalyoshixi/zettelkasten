---
tags:
  - programming
  - c
---
A small library that can perform [[Advanced Encryption Standard|AES]] encryption without windows APIs.
- Does not support padding, all buffers must be multiples of 16 bytes
- Arrays can be signatured, so ensure you XOR them before calling `AES_init_ctx_iv`
# Custom Padding Function
```c
BOOL PaddBuffer(IN PBYTE InputBuffer, IN SIZE_T InputBufferSize, OUT PBYTE* OutputPaddedBuffer, OUT SIZE_T* OutputPaddedSize) {

	PBYTE	PaddedBuffer        = NULL;
	SIZE_T	PaddedSize          = NULL;

	// calculate the nearest number that is multiple of 16 and saving it to PaddedSize
	PaddedSize = InputBufferSize + 16 - (InputBufferSize % 16);
	// allocating buffer of size "PaddedSize"
	PaddedBuffer = (PBYTE)HeapAlloc(GetProcessHeap(), 0, PaddedSize);
	if (!PaddedBuffer){
		return FALSE;
	}
	// cleaning the allocated buffer
	ZeroMemory(PaddedBuffer, PaddedSize);
	// copying old buffer to new padded buffer
	memcpy(PaddedBuffer, InputBuffer, InputBufferSize);
	//saving results :
	*OutputPaddedBuffer = PaddedBuffer;
	*OutputPaddedSize   = PaddedSize;

	return TRUE;
}
```