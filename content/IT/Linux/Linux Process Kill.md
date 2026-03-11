---
tags:
  - linux
aliases:
  - kill
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
# Sending Specific [[Signal]]
```
kill -SIGNAL pid
```
- `kill -STOP 3819`
- `kill -CONT 3819`
- `kill -INT 3819`