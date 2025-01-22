---
tags:
  - malware
  - PE
---
### Bound Import Data Directory

similar to the [[Import Directory Table|IDT]] however it holds information about [[Bound Imports]]

has an array of IMAGE_BOUND_IMPORT_DESCRIPTOR and ends with a zeroed-out IMAGE_BOUND_IMPORT_DESCRIPTOR

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivfg_tmp_b9a301fe65b9d6a1.png)

TimeDateStamp: time date stamp of the imported DLL

OffsetModuleName: offset from first IMAGE_BOUND_IMPORT_DESCRIPTOR to a string with name of imported DLL

NumberOfModuleForwarderRefs: number of IMAGE_BOUND_FORWARDER_REF structures that immediately follow this structure

IMAGE_BOUND_FORWARDER_REF is a structure identical to IMAGE_BOUND_IMPORT_DESCRIPTOR except the last member is reserved
