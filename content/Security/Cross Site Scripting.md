---
tags:
  - security
  - web
aliases:
  - XSS
---
A [[Security Vulnerability]] that allows third party code from an attacker to be ran on a user's web browser, thereby allowing credentials to be stolen and malware to be installed.
Disabling javascript on websites eliminates this vulnerability, but prevents many websites from working properly.
# Non-Persistent XSS
Non-persistent because it exploits sessions
- Website allows scripts to be ran in user input
- Attacker emails a modified link to a user
# Persistent XSS
- Attacker posts payload that is stored on the webserver
- Everybody who visits that website also gets the payload