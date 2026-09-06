---
tags:
  - security
  - web
aliases:
  - CSWSH
  - WSH
---
A [[Cross Site Request Forgery|CSRF]] attack for websocket connections where no [[Cross Site Request Forgery Token|CSRF Token]] is used for requsets.
Can be used for [[Man-In-The-Middle|MITM]] attack that places an attacker's server between the client and server's web socket connection.
- Client -> Attacker Server -> Server
Allows for two-way data manipulation:
- Manipulating client->server data
- Manipulating server->client data
# Protecting
- Use `wss://`
- Hardcode url of websocket endpoint
- Protect websocket handshake message against CSRF
- Treat data received via web socket as untrusted in both directions