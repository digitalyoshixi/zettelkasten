---
tags:
  - linux
  - x86
  - assembly
aliases:
  - x86 Linux ABI Caalling Convention
---
# Process
1. First 6 arguments are saved into general purpose registers
2. Function is called with `call <location>` & `rip` pushed
3. Space is allocated onto the stack for local variables
4. Function does work
5. Stack is restored
6. Returns by calling `ret`
7. Stack adjusted to remove arguments
# Example
With C code:
```c
__attribute__((fastcall)) void printnums(int num1, int num2, int num3){
	printf("The numbers you sent are: %d %d %d", num1, num2, num3);
}

int main(){
	printnums(1, 2, 3);
	return 0;
}
```
x86 decompilation of main() is:
```c
main:
	; stack setup
	push ebp
	mov ebp, esp
	push 3 ; immediate 3 (third argument is pushed to the stack)
	mov edx, 0x2 ; immediate 2 (second argument) is copied to edx register.
	mov ecx, 0x1 ; immediate 1 (first argument) is copied to ecx register.
	call printnums
	mov eax, 0 ; return 0
	leave
	retn
```
x86 decompilation of printnums() is:
```c
printnums:
	; stack setup
	push ebp
	mov ebp, esp
	sub esp, 0x08
	mov [ebp-0x04], ecx    ; in x86, ecx = first argument.
	mov [ebp-0x08], edx    ; arg2
	push [ebp+0x08]        ; arg3 is pushed to stack.
	push [ebp-0x08]        ; arg2 is pushed
	push [ebp-0x04]        ; arg1 is pushed
	push 0x8065d67         ; "The numbers you sent are %d %d %d"
	call printf
	; stack cleanup
	add esp, 0x10
	nop
	leave
	retn 0x04
```