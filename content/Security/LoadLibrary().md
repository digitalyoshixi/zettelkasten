---
tags:
  - security
  - windows
---
Used for [[Dynamic Linking]] when the DLL is not loaded into memory already.
```c
#include <windows.h>

int main() {
    // Load the DLL
    HMODULE hModule = LoadLibraryA("sampleDLL.dll"); // hModule now contain sampleDLL.dll's handle

}
```