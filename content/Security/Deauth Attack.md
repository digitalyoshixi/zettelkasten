---
tags:
  - security
---
An attack that involves deauthenticating all connected devices so connection hashes can be stolen upon reconnecting
# Process
1. Send disconnect packets to all networked devices
2. Sniff the 4 way handshake when devices reconnect (`eapol`)
3. Brute force crack the hash