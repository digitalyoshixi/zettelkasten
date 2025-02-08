---
tags:
  - security
  - web
aliases:
  - XSS
---
A [[Security Vulnerability|Vulnerability]] that allows injection of javascript from third parties on a webpage.

# Non-Persistent XSS
Non-persistent because it exploits sessions
- Website allows scripts to be ran in user input
- Attacker emails a modified link to a user
# Persistent XSS
- Attacker posts payload that is stored on the webserver
- Everybody who visits that website also gets the payload
# Solutions
- Disabling all javascript. May be unpleasant as most webpages require javascr