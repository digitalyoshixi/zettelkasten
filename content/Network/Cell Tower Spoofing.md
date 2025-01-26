---
tags:
  - networking
  - security
---
Using tools to spoof a cell carrier tower in an attempt to direct traffic from customers towards a server you own.
This allows an attacker to:
- Eavesdrop of conversation (even if its encrypted)
- Disable encryption
- Install [[Malware]] on a device
# Development
1. Your signal must overpower the nearby cell provider signals
# Detection
- Spoofed cell towers usually have better connection than real cell towers
- Ask nearby cell providers if they have setup a cell tower in this area
- Use a [[Cell Tower Analyzer]] to compare signals sent in the past to current signals
# Implementations
- [[Stingray]]
- [[Dirtbox]]