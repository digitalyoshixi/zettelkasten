---
tags:
  - networking
  - security
---
A tool to find [[Stale Network Address Configuration]] issues.
# Installation
- Python 3.7.4
# Capture
```
eavesarp.py capture -i eth0 -ar -dr
```
# Set Ip Address
```
sudo ip addr add 10.10.10.13/24 dev eth0
```
# Remove Ip Address
```
sudo ip addr del 10.10.10.13/24 dev eth0
```
# Listen to IP Address
- Setup [[responder]] if you want to setup a server on many protocols
```
sudo tcpdump -i eth0 -nvv "host 10.10.10.13"
```