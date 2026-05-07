---
tags:
  - security
  - windows
---
A [[Authentication Coercion|NTLM Relay Attack]]
A reflection attack to impersonate users, escalate privileges and gain admin access without requiring passwords.
Abuses the fact that system-level processes view certain domains including substrings like:
- 
Involves getting a system-level process to authenticate to a remote server appearing to be itself to get a SYSTEM-level token.
# Whitepaper
https://www.synacktiv.com/en/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025