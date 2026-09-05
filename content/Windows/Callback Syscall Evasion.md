---
tags:
  - windows
  - programming
---
A method to evade [[Endpoint Detection and Response|EDR]] hooks by using [[Callback]] to run functions. You must also ensure that your calling return address is not placed on the stack:
1. Method 1: call functions that don't return.
2. Method 2: write custom assembly to not push the return address of your `RX` area
# Custom Assembly to Not Push
```asm
section .text
extern getLoadLibraryA
global WorkCallback

WorkCallback:
	mov rcx, rdx
	xor rdx, rdx
	call getLoadLibraryA # a custom fn that returns the LoadLibraryA address
	jmp rax # instead of calling, we jump to LoadLibraryA, does not modify call stack
```