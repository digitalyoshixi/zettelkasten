---
tags:
  - security
---
A [[NTLM Reflection]] to escalate privileges and gain admin access without requiring passwords.
Abuses the fact that system-level processes view certain domains including substrings like:
- `localhost` 
- `sv1` 
Tricks processes into using local-NTLM authentication which attaches SYSTEM token by default.
# Whitepaper
https://www.synacktiv.com/en/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025