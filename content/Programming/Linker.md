---
aliases: 
tags:
  - c
  - cpp
---
after you have [[Compiler|Compiled]] your [[C++]] program and are given object files, you are going to pass it through the linker.

The linker does 3 things.
1. Turns object files into executable or library files ![[Pasted image 20231119140137.png]] 
	library files like DLLs are pieces of code packages up for use of other programs. executables are just standard programs.

2. Links object files. You will want to use the linker for most of your programs because most of your programs are going to be using the C++ standard library. the standard library includes libraries like \<iostream\>. With the libraries you have made too, you can link those as well

3. Resolves dependencies. With your linking of object files, the linker will be able to detect errors in dependencies such as missing dependencies or missing methods. The linker will abort the process if dependencies fail.
