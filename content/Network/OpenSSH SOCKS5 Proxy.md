---
tags:
  - networking
  - linux
---
# Use Server as Proxy on Specific Port
```
ssh -D 1080 user@host
```
For your given ssh server.
After enabling the connection, change your [[Brave Browser]] to be ran with
```
brave --proxy-server="socks5://localhost:1080
```
