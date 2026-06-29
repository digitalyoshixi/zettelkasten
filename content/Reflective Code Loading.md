---
tags:
  - security
aliases:
  - Reflective DLL Injection
---
An attack similar to [[Process Injection]] that involves loading [[Position Independent Executable|PIC]] directly into another running process by loading a [[Dynamic Linked Library|DLL]] with [[LoadLibrary()]].
Inspired by [[Reflection]]
# Process
- Load reflective DLL with [[LoadLibrary()]]
- Calculate own image's location
- Parse host 