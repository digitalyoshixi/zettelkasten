---
tags:
  - security
---
A tool to screenshot all websites for you to view if there is a webpage there.
# Running From [[nmap]] Scan
```
nmap -sS -T4 -F -iL httpservers.txt -oX nmap.xml
```
```
eyewitness -x nmap.xml
```