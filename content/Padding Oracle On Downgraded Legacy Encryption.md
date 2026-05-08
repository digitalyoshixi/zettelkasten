---
tags:
  - security
aliases:
  - POODLE
---
A eavesdropping vulnerability in [[Secure Sockets Layer|SSL 3.0]] 
# Vulnerability
Abuses [[Block-Cipher]] [[Message Authentication Code|MAC]] then encrypt phenomena.
# Attack
1. Start a [[Man-In-The-Middle|MITM]] between session
2. Convince server to use [[SSL Downgrade|SSL 3.0]]
3. POODLE decrypts [[Secure Sockets Layer|SSL 3.0]]