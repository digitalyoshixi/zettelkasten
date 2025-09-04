---
tags:
  - security
---
A talk by [[Wiz]].
# Notes
- Shift Left: Moving security back to the code (Left of the pipeline)
- Shifting left will prevent any account credential theft
- Attack at [[CISA 2025 Attack]] involved gaining access to a company's github code in a repo containing a AWS token
- Misconfigurations: Inital code or cloud access -> Lateral movement -> Siezing of crown jewels
- The goal for attackers is to 
- The [[Software Development Life Cycle|SDLC]] where Code -> Pipeline -> Cloud -> Runtime
- Security often expands vertically ([[Silo]])
- (Code) AppSec -> (Pipeline) DevSecOps -> (Cloud) Cloud Security -> (Runtime) SecOps Is the security pipeline
- Shifting Left:
	- Use a unified policy engine to find misconfigurations
	- Wiz started with [[Wiz Cloud]]
	- Wiz then made [[Wiz Code]]
	- Wiz then made [[Wiz Defend]]
- [[Cloud Security Maturity Framework]]
- [[Extended Berkley Packet Filter]]
- Wiz can tell you the blast radius, what an attacker has access to, how to isolate immediately
- Assets delivered by [[Content Delivery Network|CDN]] are also very risky, 'this is shifting right'