---
tags:
  - software
aliases:
  - DLL
---
Also called shared library is an executable that cannot run on its own. like u have a object file, and it has evolution tree of 2 options. executable or DLL

## Library linkage

Put simply, the segment of your program where you import the library.

A library is an archive of already compiled code. An object file may include several libraries. These are symbols inside the object file that tell the compiler that during linkage, these libraries symbolic references need to be resolved. At the moment of linkage, the compiler will link the library’s compiled code with yours and produce the final executable file/dll.