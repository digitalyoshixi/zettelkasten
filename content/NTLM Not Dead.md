---
tags:
  - security
aliases: CVE-2025-33073
---
A [[Privilege Escalation]] vulnerability that allows for [[NTLM Reflection]] over SMB.
Abuses the fact that system-level processes view certain domains including substrings like:
- `localhost` 
- `sv1` 
Tricks processes into using local-NTLM authentication which attaches SYSTEM token by default.
# Attack
1. Create a crafted [[Domain Name Server|DNS]] record like `1UWhRCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYBAAAA` to make target interpret this as a local authentication
2. [[ntlmrelayx]] caches reflected auth to enable administrative SMB session
# Whitepaper
https://www.synacktiv.com/en/publications/ntlm-reflection-is-dead-long-live-ntlm-reflection-an-in-depth-analysis-of-cve-2025
