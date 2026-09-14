---
tags:
  - programming
  - cpp
---
A [[C++]] macro for [[Win32 API]] that allows you to explicitly say that a parameter is unused.
```c
DWORD WINAPI MsgBoxPayload(IN LPVOID lpParameter)
{
	// explicitly not used
    UNREFERENCED_PARAMETER(lpParameter);

    MessageBoxA(NULL, "Executed MsgBoxPayload Function", "MaldevAcademy", MB_OK | MB_ICONINFORMATION);

    return 0x00;
}
```