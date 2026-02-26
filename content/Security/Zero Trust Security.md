---
tags:
  - security
aliases:
  - Zero Trust
  - Zero Trust Architecture
  - ZTA
---
Human trust is flawed. Assume the attacker is already inside the system.
Give everything a [[Digital Certificate|X509 Certificate]]
![[Zero Trust Security-20250711024701537.webp|666]]
# Principles
1. Never trust, always verify. Every connection attempt should be authenticated and authorized. Use [[Adaptive Identity]]
2. Implement [[Principle of Least Privilege]]. Give them the least amount of access for them to do their job
3. Assume breach. Micro segmentation through [[Planes of Operation]] and [[Policy Enforcement Point|PEP]] to allow traffic only from specific sources
# Concepts
- [[Principle of Least Privilege]]
- [[Adaptive Identity]]
- [[Planes of Operation]]
- [[Security Zone]]
	- [[Data Plane]]
	- [[Control Plane]]
- [[Policy Enforcement Point|PEP]]
- [[Threat Scope Reduction]]
# Tools
- [[Pomerium]]