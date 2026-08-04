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
eyewitness -x nmap.xml --threads 2
```
# Running With Proxy
```
eyewitness -x nmap.xml --proxy-ip 127.0.0.1 --proxy-port 9050 --proxy-type socks5
```
# Running With Extra HTTP Ports
```
eyewitness --add-http-ports 444,81 --threads 2
```