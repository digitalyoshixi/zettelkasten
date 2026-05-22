---
tags:
  - windows
  - malware
---
A technique used by [[Endpoint Detection and Response|EDR]] that involves adding jumps at the start of windows [[Dynamic Linked Library|DLL]] to route to custom code for logging this behavior.
Can be used to:
- Trace callstack of program
- Send events with [[Events Tracing Windows|ETW]]