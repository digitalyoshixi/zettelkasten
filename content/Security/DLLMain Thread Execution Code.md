---
tags:
  - programming
  - windows
---
```c
// The real payload. Executes on its own thread, after the loader lock has been released
DWORD WINAPI MsgBoxPayload(IN LPVOID lpParameter)
{
    UNREFERENCED_PARAMETER(lpParameter);

    MessageBoxA(NULL, "Executed MsgBoxPayload Function", "MaldevAcademy", MB_OK | MB_ICONINFORMATION);

    return 0x00;
}


BOOL APIENTRY DllMain(HMODULE hModule, DWORD dwReason, LPVOID lpReserved)
{
    UNREFERENCED_PARAMETER(lpReserved);

    HANDLE hThread = NULL;

    switch (dwReason)
    {
        case DLL_PROCESS_ATTACH: 
        {
            // Suppress DLL_THREAD_ATTACH & DLL_THREAD_DETACH notifications for this module
            DisableThreadLibraryCalls(hModule);

            // Hand off to a new thread and return immediately; it will not run until
            // the loader releases the DLL lock
            if ((hThread = CreateThread(NULL, 0x00, &MsgBoxPayload, NULL, 0x00, NULL)) != NULL)
                CloseHandle(hThread);

            break;
        };
        case DLL_THREAD_ATTACH:
        case DLL_THREAD_DETACH:
        case DLL_PROCESS_DETACH:
            break;
    }

    return TRUE;
}

```