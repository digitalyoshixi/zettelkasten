---
tags:
  - security
  - web
---
A [[Man-In-The-Middle|MITM]] attack based off [[Cross Site Request Forgery|CSRF]] that places an attacker's server between the client and server's web socket connection.
- Client -> Attacker Server -> Server
Allows for two-way data manipulation:
- Manipulating client->server data
- Manipulating server->client data