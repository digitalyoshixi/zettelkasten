---
tags:
  - networking
  - ctf
  - linux
---
A tool to open up a [[Websocket]] to an internet serivice.
# Expose App
```
socat TCP-LISTEN:5000,reuseaddr,fork EXEC:"/path/to/your/program"
```