---
tags:
  - security
  - active_directory
---
This is a cyber attack that targets [[Kerberos]].
# Attack
User requests a kerberos ticket for a [[Service Principal Name]] or older service.
the ticket is encrypted using a hash derived from the server accounts password.
It can later be brute forced offline, and authenticate with the powerful kerberos ticket.
# Patching
- Disable all extra features like [[Service Principal Name]] and service accounts. Ensure you hygiene routinely
- Make [[Service Principal Name]] passwords very complex
- [[Life Cycle Management]] is extremely important. If not, then