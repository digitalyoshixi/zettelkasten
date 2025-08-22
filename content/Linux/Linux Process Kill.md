---
tags:
  - linux
---
# Kill from ID
1. `ps -a`
2. `kill <pid>`
# Pkill
```
pkill "Processname"
```
# Force Pkill
```
pgrep -io "PROCESSNAME" | xargs kill 
```