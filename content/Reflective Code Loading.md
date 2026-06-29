---
tags:
  - security
aliases:
  - Reflective DLL Injection
---
An attack similar to [[Process Injection]] that involves loading [[Position Independent Executable|PIC]] directly into another running process by loading a [[Dynamic Linked Library|DLL]] with [[LoadLibrary()]].
- Creates a program image from the .text section
- Inspired by [[Reflection]]
# Process
- Load reflective DLL with [[LoadLibrary()]]
- Calculate own image's location
- Parse host process' [[Kernel32]] export table and get addresses of:
	- [[LoadLibrary()]]
	- [[GetProcAddress()]]
	- [[VirtualAlloc]]
- Allocate region of memory and load own program image, populate import address table, image recolation table, etc
- Call image's entry point with [[DLLMain]] [[DLL_PROCESS_ATTACH]]
# Problems
- Leaves a lot of data that can be signatured
# Code
- https://github.com/stephenfewer/ReflectiveDLLInjection/