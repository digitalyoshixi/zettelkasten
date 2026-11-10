---
tags:
  - web
  - security
  - ai_safety
---
A attack against LLMs that involves using prompt injection to trigger privileged LLMs to post privileged data on public sources.
# Example
1. Scanner retrieves data from comment field left by attacker
2. Prompt directs LLM to post sensitive data to a location visible to the attacker (i.e comment or feedback field)