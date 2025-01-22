---
tags:
  - malware
  - PE
---

means that the [[Import Directory Table|IDT]] contains fixed addresses for imported functions

using bound imports is a speed optimization. reduces time needed by loader to resolve function addressess and fill the [[Import Address Table|IAT]].

If however, at run-time the bound addressess do not match the real ones. the loader has to resolve these on its own and fix the IAT

If the TimeDateStamp or another bound-based field is set to an unusual value, the real value can be found in the [[Bound Import Data Directory]]

