---
tags:
  - windows
  - malware
aliases:
  - DLL Hooking
  - API Hooking
---
A technique used by [[Endpoint Detection and Response|EDR]] that involves adding jumps at the start of windows [[Dynamic Linked Library|DLL]] to route to custom [[Trampoline Code|Trampoline]] to log behavior.
![[EDR Function Hooking-20260622154214802.webp]]
Can be used to:
- Trace callstack of program
- Send events with [[Events Tracing Windows|ETW]]