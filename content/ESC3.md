---
tags:
  - security
---
An attack against [[Active Directory Certificate Services]] that can cause [[Privilege Escalation]].
Exploits [[Active Directory Enrollment Agent]] to enroll new certificates with higher privileges.

# Finding w
# Attack Process
1. Obtain a [[Active Directory Enrollment Agent]] certificate ([[Object Identifier|OID]] 1.3.6.1.4.1.311.20.2.1)
	1. A certificate template is created specifically for Enrollment Agents
	2. A [[ESC2]] attack allows creation
2. A target certificate that allows authentication configured to allow enrollment agents to request certs on behalf of other users
	1. The target user must have enrollment rights on the target template
	2. Template allows authentication (Client auth [[Extended Key Usage|EKU]], Smart card [[Extended Key Usage|EKU]], etc)