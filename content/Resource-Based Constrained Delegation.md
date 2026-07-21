---
tags:
  - security
  - windows
aliases:
  - RBCD
---
[[Constrained Delegation]] that sets in the object who is able to impersonate any user against it.
Works with:
- [[Volume Shadow Copy]]
# Process
1. Create a new computer account
2. Setup the RBCD property on the DA to allow RBCD from the new computer account
3. Create a ticket using new computer account with kerberos targeting the DC
4. You now have access to the DC