---
tags:
  - security
aliases:
---
A [[Simple Network Management Protocol|SNMP]] tool to send requests.
# Installation
```
sudo pacman -S swaks
```

```
sudo apt install swaks
```
# Usage
```
swaks --to test@yourdomain.com --from you@yourdomain.com --server 192.168.2.75 --port 587 -tls -au username -ap password
```
# Testing for Open Relays
```
swaks --to "target@carbirdcorp.net" --from "admin@lassocrm.com" --server mailserver.com --header "From: admin@lassocrm.com" --header "To: <target@catbirdcorp.net>" --header 'Content- Type: text/plain' --body 'This is a test mail'
```