---
tags:
  - networking
---
Runs on UDP port `1701`
Provides [[Network Messages|Packet]] encryption for the [[TCP & IP Data Layer|Data Layer]].
# [[Key Exchange Protocol|IKE]] Phrase
- Uses [[Diffie Hellman Key Exchange|DHKE]] over [[User Datagram Protocol|UDP]] port `500`
# Process
1. [[Key Exchange Protocol|IKE]] exchange over [[User Datagram Protocol|UDP]] `500`
2. IPSec tunnel creation with either:
	1. [[Authentication Header|AH]] to provide authentication and integrity
	2. [[Encapsulating Security Payload|ESP]] to provide auth, integrity and encryption
3. Data sent via [[IPSec Modes|Tunnel Mode]], [[IPSec Modes|Transport Mode]] or [[IPSec Modes|Always-on-Mode]]
# Concepts
- [[IPSec Modes]]
- [[IPSec Packet]]
- [[Perfect Forward Secrecy|PFS]]
- [[Security Associations|SA]]
- [[Security Association Database|SAD]]
- [[Security Policy Database|SPD]]
- [[Authentication Header|AH]]
- [[Encapsulating Security Payload|ESP]]