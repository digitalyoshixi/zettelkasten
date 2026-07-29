---
tags:
  - security
---
A talk at [[Toronto Area Security Klatch|TASK]] by Stephen Litvack.
# Notes
- [[Business Resilience]]
- Pitfalls if you dont have a well laid plan, may not even test their plans, these are the problems, its all about making plans well
- Worst case scenario is not when you don't have a plan, its when your plan fails
	- Waste time on a plan that doesn't make sense, you're better off going with your gut
- Very uncommon to see clear defined lines for when to identify disasters
	- Senior leadership may not know when a disaster is even happening, massive gap
- TTC very close to strike, impacts the business continuity plan immensely
- [[Business Impact Analysis|BIA]] and [[Business Continuity Plan|BCP]]/[[Disaster Recovery|DRP]] development process
- [[Business Impact Analysis|BIA]] is disruption impact
	- Identify business processes
	- Assess impact to business if process is disrupted
	- Determine process requirements
- [[Business Continuity Plan|BCP]] is for continuing operations
	- Define BCP activation criteria tied to [[Mean Time to Fail|MTTF]] ([[Recovery Time Objective|RTO]])
	- Establish organization roles and responsibilities (if you want this to actually work)
	- Develop workarounds to continue prioritized processes to minimum viable level
	- Develop procedures to return operations to business as usual following a disruption
- [[Disaster Recovery|DRP]] is for recovery technology
	- Define DRP activation criteria tied to max tolerable downtime of technical dependencies
	- Establish roles to recover technology upon disruption
	- Develop recovery procedures to restore critical technology
	- Re-certify procedures to validate system recovery by confirming system functionality