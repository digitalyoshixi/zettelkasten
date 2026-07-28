---
tags:
  - redteam
---
This is a scanning tool built into kali linux. This allows discover of devices in a network.
# Host and Port Scanning
```
nmap -p 1-65535 192.168.2.1-255
```
# Full Scan
```
nmap -sS -T4 -F <target>
```
# RDP Encryption Enumeration
```
nmap -p 3389 --script rdp-enum-encryption 192.168.1.186
```