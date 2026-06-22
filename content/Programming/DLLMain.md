---
tags:
  - programming
---
This is the entry point of a [[Dynamic Linked Library|DLL]].
Can be ran with 4 cases:
- `DLL_PROCESS_ATTACH` - A process is loading the DLL.
- `DLL_THREAD_ATTACH` - A process is creating a new thread.
- `DLL_THREAD_DETACH` - A thread exits normally.
- `DLL_PROCESS_DETACH` - A process unloads the DLL.
```c
// Entry point for the DLL
BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
        case DLL_PROCESS_ATTACH:
        case DLL_THREAD_ATTACH:
        case DLL_THREAD_DETACH:
        case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}
```