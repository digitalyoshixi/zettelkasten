---
tags:
  - programming
  - windows
---
# Exports
```c
__declspec(dllexport) VOID MsgBoxPayloadExp(VOID)
{
    MessageBoxA(NULL, "Executed The Exported MsgBoxPayload Function", "MaldevAcademy", MB_OK | MB_ICONINFORMATION);
}
```