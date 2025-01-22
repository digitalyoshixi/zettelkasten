---
tags:
  - networking
aliases:
  - RR
---
# Records
### Address Records (A and AAAA)
Record that can store human-friendly aliases for [[IP Address]].
A-level records alias names to [[IPv4]]
AAAA-level records alias names to [[IPv6]]
Example:
```c
www.goatse.org IN A 153.167.98.165 ; my favorite website lol
www.peatersites.ca IN AAAA 127.89.54.12 ; im gonna ddos this 
```
### Mail Exchange (MX) Records
Aliasing names to mail server addresses.
Example:
```c
IN MX www.theblackmarket.com
www.theblackmarket.com IN A 126.45.165.90 ; love this place
```
### TXT Records
Public information that can be accessed by anyone on the internet.
**NOT** used to direct traffic.
Often used as a junk drawer of DNS database. Used to store miscellaneous items and spam.
Spam is outlined with [[Domain Keys Identification Mail|DKIM]], [[Sender Policy Framework|SPF]] and [[Domain-based Message Authentication, Reporting and Conformance|DMARC]] records
# Time To Live (TTL)
How long these records are cached in on user's local device.
Once this cache expires and is removed, the user will have to request the DNS server again.