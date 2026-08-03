---
tags:
  - programming
  - web
---
Continuous streams of communications that provide real-time data.
A websocket request must first be sent, then a different protocol is used to allow a continuous stream of TCP/IP data. Its [[Point-to-point Communication|Full Duplex]] communication.
# Protocol
1. Send the websocket handshake with the server with websocket key and version
2. Server responds with `101` and protocol upgrade
3. Websocket connection starts
# Tools
- [[websocat]]
- [[Socket.io]]