---
tags:
  - security
aliases:
  - impacket-mssqlclient
---
A [[Microsoft SQL]] client.
```
impacket-mssqlclient $USER:$USERPASS@$DCIP -windows-auth
```
# Enumerating Links
```
enum_links
```
# Using a Share
```
use_link FOUNDSQLSTG01
```
# Changing to a Different Database
```
exec xp_cmdshell 'whoami'
```