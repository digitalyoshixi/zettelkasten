---
tags:
  - nixos
aliases:
  - SMB
  - CIFS
  - Common Internet File System
---
A Secure Protocol operating at [[TCP & IP Application Layer|Application Layer]] used to share:
- Files
- Printers
- Serial ports
- ETC
Between [[Windows]] devices on a network.
Relies on [[Transmission Control Protocol|TCP]] and [[Internet Protocol|IP]] for transfers.
- Modern systems use SMB on `tcp/445`
- Older systems use the [[NetBIOS|NetBIOS]] protocol
Uses [[New Technology LAN Manager|NTLM]] for authentication.
# Protocol
1. [[NetBIOS]] session is created between server and cient
2. Server and client negotiate SMB protocol version
3. Client logs on to server with proper credentials
4. Client connects to shared resource hosted on server, opens, reads, edits, shares, etc
# Versions
- [[SMB 1.0]]
- [[SMB 3.1]]
# Implementations
- [[Windows File and Printer Sharing]]
- [[Common Internet File System]]
- [[Samba]]