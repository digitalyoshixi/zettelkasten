---
tags:
  - windows
  - win32api
---
The windows API is weird because of window's insistence on backwards compatibility.
# VSCode Project Configuration
- Solution > Properties > Platform > All Platforms
- Solution > Properties > Configuration Properties > Advanced > Character Set > Use Multi Byte Character Set
- Solution > Properties > Linker > System > Subsystem > Windows
# Concepts
- [[windows.h]]
- [[Win32 API Naming Conventions]]
- [[Instance Handle|HInstance]]
- [[Long Strings]]
- [[Handle Device Context|HDC]]
- [[Graphics Device Interface|GDI]]
- [[Out Parameters]]
- [[Windows System Error Codes]]
- [[NTSTATUS]]
### Quick Startup
http://www.winprog.org/tutorial/start.html
- [[Win32 API Boilerplate Program]]
- [[Win32 API Simplest Program]]
# DataTypes
- [[DWORD]]
- [[size_t]]
- [[Handle]]
- [[Module]]
# Useful Functions
- [[WinMain()]]
- [[MessageBox()]]
- [[VirtualAlloc]]
- [[VirtualFree]]
- [[VirtualProtect]]
- [[RtlIpv6StringToAddress]]
- [[CreateWindow]]
- [[GetProcAddress()]]
- [[GetModuleHandle()]]
- [[HeapAlloc()]]
- [[LocalAlloc()]]
- [[HeapFree()]]
- [[LocalFree()]]
- [[GetLastError()]]
# Guides
- https://github.com/7etsuo/windows-api-function-cheatsheets