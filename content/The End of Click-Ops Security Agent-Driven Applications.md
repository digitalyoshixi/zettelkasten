---
tags:
  - books
  - security
---
A security talk about [[AI Agent|AI Agents]] at [[TASK]].
# Notes
- [[Software as a Service|SaaS]] is DEAD because of [[AI Agent|Agentic AI]]
- AI is on the boom, exponential amount of AI projects on [[Github]] and models on [[Huggingface]]
- [[Large Language Model|LLM]] < [[AI-Native Applications]] < [[AI Agent]]
- There are higher stakes with AI agents since they have write operations
- Modern threats for applications:
	- [[Large Language Model|LLM]]:
		- Prompt injection
		- Harmful content
	- [[AI-Native Applications]]:
		- Data leakage
		- Unauthorized access 
	- [[AI Agent|AI Agents]]:
		- Autonomous Chaos
- Cloud is still more risky than AI
	- Capitalone lost millions from bad EC2 configuration
- [[AI Security]]
- Most [[Retrieval Augmented Generation|RAG]] will still contain sensitive data
- Most if not all [[Large Language Model|LLMs]] will have [[AI Alignment]] to prevent obviously harmful prompts (like, asking for a users credit card number) by default
- AI is [[Stochastic Algorithm]], and you can often get different results from the same input
- AI can be used in [[Cross Site Scripting|XSS]] attacks and [[Cross Site Request Forgery|CSRF]] to visit attackers sites
- AI Agents Diagram:
![[Drawing 2025-05-28 19.53.25.excalidraw]]
- Its not like cloud where there is an agreement for the end-user to manage security.
- Model security is the providers responsibility
- We have to secure data pipelines, prompt layer on our user end
- [[Model Context Protocol]]
- [[Agent to Agent Protocol]]