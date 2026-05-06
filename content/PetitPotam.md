---
tags:
  - security
  - windows
aliases:
  - MS-EFSRPC
---
A PoC exploiation tool that abuses [[Encrypting File System|EFS]]s insufficient path checks in `EfsRpcOpenFileRaw` to allow any user to become windows domain admin. 
Uses NTLM relay to force a sever to authenticate with an attacker's system.
