---
tags:
  - security
---
A [[Endpoint Detection and Response|EDR]] technique to bypass [[DLL Injection|DLL Sideloading]] by checking if the last stack frame (return address) is in a `RX` region.
![[EDR Last Stack Call Tracing-20260522171842215.webp]]
Bypassed if you use [[Callback Syscall Evasion]]