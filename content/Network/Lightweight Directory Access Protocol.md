---
tags:
  - networking
aliases:
  - LDAP
---
Vendor neutral protocol used for viewing and querying directories.
Conventionally seen on port `tcp/389`.
Secure version on `tcp/636` ([[Lightweight Directory Access Protocol over Secure Sockets Layer|LDAPS]])

Can be used to:
- Query online directories of users, devices, etc
- Authenticate users by looking at an authentication directory like [[Windows Active Directory]], [[Terminal Access Controller Access-Control System Plus|TACACS+]] or [[Remote Authentication Dial-In User Service|RADIUS]]
# Implementations
- [[Windows Active Directory]]
# Alternatives
- [[Lightweight Directory Access Protocol over Secure Sockets Layer]]
# Resources
- https://fy.blackhats.net.au/pages/the-ldap-guide-part-1-foundations/
- https://www.zytrax.com/books/ldap/