---
tags:
  - security
---
A talk by Shashank Golla at [[Wiz]]
# Notes
- Known threats:
	- [[Front-Door Access]]
	- Excessive [[Identity and Access Management|IAM]] permissions and [[Lateral Movement]]
	- [[Supply Chain Vulnerability|Supply Chain Attack]]
- [[Elastic Kubernetes Service]] exposed, and then exploited in less than 20 minutes
- [[Deepseek Dataleak]]
- Over 85% of organizations are using some form of AI:
	  [[Langchain]]
	  Hugging face
	  OpenAI
	  Tensorflow
- Threats from vibe coding
- AI as infrastructure, acceleration without control (No [[AI Governance]])
- [[ASPM]] systems to check for [[Static Application Security Testing|SAST]] and [[Dynamic Application Security Testing|DAST]]
- [[CSPM Scanner]]
- How do we know the developer who pushed the code to te cloud? This will increase time of remediation
- For run-time, we use [[Endpoint Detection and Response|EDR]]
- Wiz will run risk assessments for everything like:
	- Open secrets
	- Vulnerabilities
	- Identity
	- Configuration
	- Data and AI
	- Public exposure
- Customers will attempt to use Wiz for:
	- Proactive approach to run risks assessments of [[AI Agent]]
	- Runtime security with [[Wiz Sensor]]
	- Cloud-to-code graph tracing a resource to a repo
	- Checking [[Identity and Access Management|IAM]]
	- Developing security guardrails early in te lifecycle
- Starting from the [[Integrated Development Environment]] that [[Wiz Code]] acts as a extension, has guard rails
- Wiz security cloud can view from [[Terraform]] file, so that you can actually see any exposed cloud services
- Wiz allows for Democratization