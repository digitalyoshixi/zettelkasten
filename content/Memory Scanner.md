---
tags:
  - security
  - malware
---
Tools that scan the memory of a process to identify non-standard attributes within the memory region.
# [[Indicator of Compromise|IOC]]
- `RWX` memory segment
- Non-[[Clean Stack]]
- High [[Shannon Entropy]] in file
	- Encryption increases entropy
	- [[Globally Unique Identifier|UUID]] as encoding does not increase entropy
# Triggers
Memory scanners are triggered periodically or after certain events:
- [[PsSetCreateProcessNotifyRoutine]]
- [[PsSetCreateThreadNotifyRoutine]]
- [[PsSetLoadImageNotifyRoutine]]
Or certain sensitive APIs are called:
- [[NtAllocateVirtualMemory]]
- [[NtWriteVirtualMemory]]
- [[NtProtectVirtualMemory]]
- [[NtCreateThreadEx]]
- [[NtMapViewOfSection]]
# Tools
- https://github.com/hasherezade/pe-sieve
- https://github.com/forrest-orr/moneta
- https://github.com/thefLink/Hunt-Sleeping-Beacons