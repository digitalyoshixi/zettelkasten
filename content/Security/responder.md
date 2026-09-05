---
tags:
  - windows
  - security
---
A tool for [[LLMNR Poisoning]].
Can capture [[New Technology LAN Manager|NetNTLM Hash]]
```
responder -I networkinterface
```
- Run in monitor mode
- Relay specific ip
# Example
```
responder -I eth0
```
You can find these interface with `ip link` or [[ifconfig]]