---
tags:
  - security
---
A talk by [[Wiz]].
# Notes
- Shifting left will prevent any account credential theft
- Attack at CISA involved gaining access to a company's github code in a repo containing a AWS token
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