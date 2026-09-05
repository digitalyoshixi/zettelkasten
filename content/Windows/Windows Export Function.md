---
tags:
  - windows
---
Must be set with `extern` and `__declspec(dllexport)`
```c
extern __declspec(dllexport) void HelloWorld(){
    MessageBoxA(NULL, "Hello, World!", "DLL Message", MB_ICONINFORMATION);
}
```