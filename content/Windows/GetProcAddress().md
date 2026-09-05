---
tags:
  - windows
  - win32api
---
A [[Win32 API]] function to get the address of a function in a [[Dynamic Linked Library|DLL]].
```c
FARPROC GetProcAddress(
  [in] HMODULE hModule,
  [in] LPCSTR  lpProcName
);
```
- `hModule` can be gotten from [[GetModuleHandle()]] or [[LoadLibrary()]]
- `lpProcName` is the string name of the function
# Example
```c
#include <windows.h>

// Constructing a new data type that represents HelloWorld's function pointer 
typedef void (WINAPI* HelloWorldFunctionPointer)();

void call() {
    // Attempt to get the handle of the DLL
    HMODULE hModule = GetModuleHandleA("sampleDLL.dll");
    if (hModule == NULL) {
        // If the DLL is not loaded in memory, use LoadLibrary to load it
        hModule = LoadLibraryA("sampleDLL.dll");
    }
	// pHelloWorld stores HelloWorld's function address
    PVOID pHelloWorld = GetProcAddress(hModule, "HelloWorld"); 
    // Typecasting pHelloWorld to be of type HelloWorldFunctionPointer
    HelloWorldFunctionPointer HelloWorld = (HelloWorldFunctionPointer)pHelloWorld;
	// Invoke HelloWorld
    HelloWorld();
}

int main(){
  call(); // Invoke the call() function
  return 0;
}
```