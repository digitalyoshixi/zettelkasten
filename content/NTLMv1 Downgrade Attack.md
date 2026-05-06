---
tags:
  - security
  - windows
---
An [[Privilege Escalation]] attack against [[New Technology LAN Manager|NTLM]] authentication that involves sending your allowed protocols to only be [[NTLMv1]] so that the server must communicate in an insecure way.
Can later be used in a [[Pass The Hash Attack]]
# Cracking
Grab the hashes from [[responder]] and then crack with [[Hashcat]]
- https://hashcat.net/forum/thread-9009.html
```
./hashcat -m 14000 -a 3 -1 charsets/DES_full.charset --hex-charset 14000.hash ?1?1?1?1?1?1?1?1
```
# Countermeasures
Configure network security LAN Manager Authentication Level to send NTLMv2 responses only.
- Modify registry key `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Lsa\LmCompatibilityLevel` to 3,4 or 5 (preferably 5)