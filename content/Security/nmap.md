---
tags:
  - redteam
---
This is a scanning tool built into kali linux. This allows discover of devices in a network.
# Host and Port Scanning
```
nmap -p 1-65535 192.168.2.1-255
```
# Quick Stealth Scan
```
nmap -sS -T4 -F <target>
```
# RDP Encryption Enumeration
```
nmap -p 3389 --script rdp-enum-encryption 192.168.1.186
```
# From Input File, to Output File
```
nmap -sS -T4 -F -iL httpservers.txt -oX nmap.xml
```