---
tags:
  - windows
  - security
aliases:
  - Stack Detection
---
A stack that is comprised of stack frames wherein:
- Each stack frame should be expected to be within the right memory space
- Specific functions should not be issued from certain memory regions
	- [[LoadLibrary()]] should not be called in relation to a `MEMPRIVATE + RX` space
# Elastic Rules for Stack Layout
```json
process.thread.Exr.call stack summary in
	("ntdll.dll|kernelbase.dll|ntdll.dll|kernel32.dll|ntdll.dll",
"ntdll.dll|wow64.dll|wow64cpu.dll|wow64.dll|ntdll.dll|kernelbase.dll|ntdll.dll|kernel32.dll|ntdll.dll"	
)
```