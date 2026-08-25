---
tags:
  - windows
  - security
aliases:
  - CBT
---
A [[Lightweight Directory Access Protocol over Secure Sockets Layer|LDAPS]] specific feature that binds a `Channel Binding Token` (unique identifier) to a specific TLS tunnel with your target device.
# Implementing
```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\NTDS\Parameters\LdapEnforceChannelBinding
```
- (0) Never (default, no CBT)
- (1) When Supported (audit; emits failures but doesn't block)
- (2) Always (enforces; rejects binds without CBT)
# Implementing on Older Systems
1. Install windows CVE-2017-8563 if system older than 2017 (https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2017-8563)
2. Install August 2023 KB4320412 update if server 2019, 2022 (https://support.microsoft.com/en-us/topic/2020-and-2023-ldap-channel-binding-and-ldap-signing-requirements-for-windows-kb4520412-ef185fb8-00f7-167d-744c-f299a66fc00a)
3. Configure GPO settings on DC:
	1. Domain controller: LDAP server channel binding token requirements = "Always"
# Auditing
- Assuming [[Windows Enable LDAP Diagnostics]] setup.
- Can only audit effectively when LDAP channel binding set to "When supported"
[[Windows Event Viewer]] logs:
- `3039`: Client did not provide CBT during authentication process
- `3074`: LDAPS bind would have failed CBT validation if enforced
- `3075`: LDAPS bind omitted CBT data and rejected if enforced
