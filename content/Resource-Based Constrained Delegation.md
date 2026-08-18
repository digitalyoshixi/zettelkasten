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
# Requirements
1. Must have control over an SPN
2. Permission to write to `msDS-AllowedToActOnBehalfOf` attribute
	1. GenericAll
	2. GenericWrite
	3. WriteOwner
	4. WriteDACL
	5. AllExtendedRights
	6. ForceChangePassword
	7. Self (Self Membership)
# Process
![[Resource-Based Constrained Delegation-20260818025350777.webp]]
1. Create a new computer account
2. Modify `msDS-AllowedToActOnBehalfOfOtherIdentity` property of an object to allow RBCD from the new computer account
3. Create a administrator [[Ticket Server|TGS]] using new computer account with kerberos targeting the DC using [[S4U2Self]]
4. Request administartor [[Ticket Server|TGS]] for target through [[S4U2Proxy]]
5. You now have access to the DC
# Attack
- [[impacket-rbcd]]
