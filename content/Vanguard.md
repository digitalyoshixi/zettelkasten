---
tags:
  - security
---
A [[Anticheat]]
# Features
- Loads at windows boot, sees all driver loads
- [[Kernel Callback]]
	- Syscall hooking
	- SwapContext (context switch monitor)
	- IAT hooks
	- `Device\\VGK_PLZNOHACK`
- [[VMProtect]]
- [[Packman]]
- Guarded regions
- Anti-debuggers
- Anti-hypervisors
- Anti-[[Direct Memory Access|DMA]]
- Anti-screen capture
- Return address verification (Calling from unexpected location = flagged)
- [ ] Bcrypt import for signature verification of loaded code