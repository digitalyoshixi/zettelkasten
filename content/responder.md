---
tags:
  - windows
  - security
---
A tool for [[LLMNR Poisoning]]
```
responder -I networkinterface
```
# Example
```
responder -I eth0
```
You can find these interface with `ip link` or [[ifconfig]]