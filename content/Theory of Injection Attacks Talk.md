---
tags:
  - security
---
# Notes
- Input attacks include:
	- [[Insecure Deserialization]]
	- Allowing arbitrary inputs outside of specification
	- Command injection
- [[Language-Theoretic Security|LangSec]] notes that everything approaches a weird machine as systems become more complex
- [[Property Oriented Programming|POP]] and [[Return Oriented Programming|ROP]] allow weird machines
- [[Double Encoding]]
# Papers
- [[Language-Theoretic Security|LangSec]] : 
- https://dl.acm.org/doi/epdf/10.1145/3485500
- https://tractable.for-all.dev/problems/agent-weirdmachines
- https://www.cs.ru.nl/~erikpoll/ss/2020/slides/7_InputProblems.pdf
# Project Ideas
### High
- Weird machine database creator, as a smart fuzzer to find inputs that can cause memory primatives to exploit weird machines
- Automata learning for web security - how to reveal any website's backend
	- A re-look at [[L*]] algorithm and how it can be improved in modern day. Mapping out web security backend via state machine, errors, side channel, application fingerprints, etc
	- You can check for bypasses of business logic flows
	- https://medium.com/@edi.muskardin/automata-learning-a-gentle-introduction-82f7ec21d50d
	- https://www.cs.ru.nl/~erikpoll/papers/langsec2015.pdf
### Medium
- Semgrep rules to find [[Shotgun Parser]]
### Low
- Automatic grammars for types based off use ([[Trusted Types]])
- Overview of langsec ideas