---
tags:
  - verification
  - machine_learning
  - software
  - programming
---
A talk at [[Association of Computing Machinery]]
# Notes
- [[Type L Advantage]]
- [[Type E Advantage]]
- [[Bullshit Avoidance Discipline|BAD]]
- Tons of Gen-AI linked mishaps
	- Amazon.com disruption with 120000 orders lost
	- Georgia tech 35 new CVE every month directly attributed to AI coding tools
	- 20% AI code references packages dont exist
	- 1.78M exploit hit Moonwell DeFi protocol with Claude as co-author
	- Lighturn 43% AI generated code changes require manual debugging
	- Sherlock forensic audit of AI generated codebase 92% one critical vulnerability
- Provably -> Probably
- Even if each module 99.9% correct independently, probability that 1000 composition is correct is 37%, probability that 5000 modules correct < 1%
- Autoproof environment created as such
	- ![[ACM Software Verification in the World of AI-20260508002320216.webp]]
	- Uses [[Eiffel]] to enforce contracts\
- Agents still fail in producing verified code
- You need a entire process involving the human who still is a little more powerful than AI
- We require AI as a process
- His paper: https://arxiv.org/abs/2601.16239