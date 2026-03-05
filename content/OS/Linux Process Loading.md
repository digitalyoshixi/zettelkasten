---
tags:
  - os
  - linux
---
A [[Linux Process]]
# Process
### Creation
- Parent process copies itself with [[fork()]] or [[clone]]
- Child process calls [[execve]] to replace itself with the actual process it should be
### Loading
- [[OS/Kernel]] checks if we have executable permissions for this file. If the file is not executable, then [[execve]] will fail.
- If the file starts with [[shebang]], then it is treated like a [[Bash]] script
- If file matches a format in [[Linux Miscellaneous Binary Format]] (`/proc/sys/fs/binfmt_misc`), kernel executes interpreter for that specific format
- If file is a [[Dynamic Linking|Dynamically Linked]] [[Executable and Linkable Format|ELF]], kernel reads interpreter/loader defined in the ELF, and lets that interpreter take control. ([[Linux View File Interpreter]])
- If file is [[Static Linking|Statically Linked]] [[Executable and Linkable Format|ELF]], kernel loads it directly
- Other legacy file formats are checked
### Dynamically Linked ELF Library Loading Process
1. Program and interpreter loaded by kernel
2. Locate libraries:
	- Check [[LD_PRELOAD]] environment variable
	- Check anything in /etc/ld.so.preload
	- Check [[LD_LIBRARY_PATH]] environment variable for all [[Shared Object]] in there
	- check DT_RUNPATH or DT_RPATH
	- Check system wide conf /etc/ld.so.conf
	- Check /lib and /usr/lib
	- Interpreter loads the libraries
3. Interpreter loads libraries
### Statically Linked ELF Library Loading Process
1. Libraries are directly inserted into the final memory space
### Virtual Memory Space Allocation
Each linux process gets a [[Virtual Memory Space]]
### Initialization
- [[C Constructor|Constructors]] are setup that run before the program is actually launched