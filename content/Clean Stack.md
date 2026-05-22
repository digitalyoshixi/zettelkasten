---
tags:
  - windows
  - security
---
A stack that is comprised of stack frames wherein:
- Each stack frame should be expected to be within the right memory space
- Specific functions should not be issued from certain memory regions
	- [[LoadLibrary()]] should not be called in relation to a `MEMPRIVATE + RX` space