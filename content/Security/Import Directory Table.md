---
tags:
  - malware
  - PE
aliases:
  - IDT
---
Part of the [[Section Table]] located at the .idata segment.
# Format
OriginalFirstThunk: RVA of the ILT

TimeDateStamp: timestamp thats set to 0 if not bound and -1 if bound

ForwarderChain: index of first forwarder chain reference. responsible for DLL forwarding(when a DLL forwards some exported functions to another DLL)

Name: [[Relative Virtual Addressing|RVA]] of Ascii that contains name of imported DLL

FirstThuhk: [[Relative Virtual Addressing|RVA]] of [[Import Address Table|IAT]]

IDT uses [[Bound Imports]]