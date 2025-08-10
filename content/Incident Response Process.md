---
tags:
  - security
aliases:
  - IR Process
---
![[Incident Response Process-20250810013039588.webp|388]]
# Process
### Preparation
- Organizations establish [[Incident Response Plans]]
- [[Cybersecurity Incident Response Team]] is established
- System configurations, [[Network Topology Diagram]], inventory of critical assets are documented
### Detection
- Setup [[Endpoint Detection and Response|EDR]] on network endpoints
- Setup [[Intrusion Detection System|IDS]]
- Set up logging with a [[Syslog]] server
- Setup [[Security Information and Event Management|SIEM]]
### Analysis
- [[Security Information and Event Management|SIEM]] analyzes for correlations and anomalies
- We can use [[MITRE ATT&CK]], [[Cyber Kill Chain]] or [[Diamond Model of Intrusion Analysis]] to categorize severity of incident
### Containment
- Isolate and [[Quarantine]] affected systems
- Compromised user accounts and credentials should be disabled
- Volatile evidence like running processes, network connection should be collected for future analysis
### Eradication
- Destroy the root cause of incident. If its malware, then purge it
- Delete infected files
- [[Patching]]
- Protect environment against future attacks
### Recovery
- Restore operations to a normal state