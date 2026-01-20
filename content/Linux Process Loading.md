---
tags:
  - os
  - linux
---
A [[Linux Process]]
# Process
### Creation
- Parent process copies itself with [[fork]] or [[clone]]
- Child process calls [[execve]] to replace itself with the actual process it should be
### Loading
- [[OS/Kernel]] checks if we have executable permissions for this file. If the file is not executable, then [[execve]] will fail.
- If the file starts with [[shebang]], then it is treated like a [[Bash]] script
- If file matches a format in `/proc/sys/fs/binfmt_misc`, kernel executes interpreter for that specific format
- If file is a [[Dynamic Linking|Dynamically Linked]] [[Executable and Linkable Format|ELF]], kernel reads interpreter/loader defined in the ELF, and lets that interpreter take control.
- If file is [[Static Linking|Statically Linked]] [[Executable and Linkable Format|ELF]], kernel loads it directly
- Other legacy file formats are checked