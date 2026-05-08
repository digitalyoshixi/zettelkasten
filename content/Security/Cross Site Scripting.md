---
tags:
  - security
  - web
aliases:
  - XSS
---
A [[Security Vulnerability|Vulnerability]] that allows injection of javascript from third parties on a webpage.
# Non-Persistent/Reflective XSS
Non-persistent because it exploits sessions
- Website allows scripts to be ran in user input
- Attacker emails a modified link to a user
### Example:
A site has a user input field that returns a paragraph tag with the input inside it. If a user inputs javascript. it can be arbitrarily ran.
![[Cross Site Scripting-20250208013518414.webp|499]]
### Example2:
```
https://site.com/search?q=
```
# Persistent/Stored XSS
- Attacker posts payload that is stored on the webserver
- Everybody who visits that website also gets the payload
![[Cross Site Scripting-20250208013845670.webp|720]]
# Solutions
- Disabling all javascript. May be unpleasant as most webpages require javascript to function
- Setup input validation
- Setup output encoding