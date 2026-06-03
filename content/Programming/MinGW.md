---
tags:
  - cpp
  - windows
---
A toolchain of header files to allow [[Low Level Virtual Machine|LLVM]], [[GCC]] to work on windows.

1. Download https://www.msys2.org/
2. `pacman -Syu` in the msys2 terminal
3. `pacman -S mingw-w64-x86_64-gcc`
4. `pacman -S mingw-w64-x86_64-gdb`
5. add path `C:\msys64\mingw64\bin` to the [[Windows PATH]]
open your terminal. check if `gcc --version` works