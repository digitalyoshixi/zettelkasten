---
tags:
  - networking
aliases:
  - FTPS
---
A protocol that uses [[Transport Layer Security|TLS]] to setup secure tunnels for [[File Transfer Protocol|FTP]] sessions.
Has two modes:
- Implicit (Negotiates a secure session) 
- Explicit (Requires a secure session) 
Uses `tcp/990` for the control channel and `tcp/998` for the data channel.