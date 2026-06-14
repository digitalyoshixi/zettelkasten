---
tags:
  - security
aliases:
  - EAC
---
Industry standard [[Anticheat]].
- Kernel level 
# Features
- [[Kernel Callback]]
	- PsSetCreateProcessNotifyRoutine: Sees every process creation
	- PsSetLoadImageNotifyRoutine: Sees every DLL/driver load
	- PsSetCreateThreadNotifyRoutine: Sees every thread creation
	- ObRegisterCallbacks: Intercepts handle operations
	- Minifilter: Filesystem monitoring
	- CmRegisterCallbackEX: Registry monitoring
	- Each callback also strips access rights (No PROCESS_VM_READ, PROCESS_VM_WRITE, PROCESS_CREATE_THREAD)
- [[Memory Scanner]]
- [[Device Driver|Drivers]] validation
- Stack walking detection via [[RtlVirtualUnwind]]
- [[System Service Descriptor Table|SSDT]] integrity via [[IA32_STAR]] MSR
- Bootstrapper downloads fresh client modules from [[Content Delivery Network|CDN]] every launch