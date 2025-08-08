---
tags:
  - security
  - networking
aliases:
  - SIEM
---
A [[Server]] for storing logs and events.
Requires a large drive array.
It is best to have [[Large Language Model]] to filter logs or implement smart [[Alert Tuning]].
# Features
- Data collection with [[Simple Network Management Protocol|SNMP]], [[WMI]], [[Internet Control Message Protocol|ICMP]], [[Hyper Text Transfer Protocol|HTTP]]
- Aggregates all data and removes duplicates
- Data correlation between events
- Generates alerts if it finds noteworthy correlations or events
# Techniques
- [[Command Line Auditing]]
