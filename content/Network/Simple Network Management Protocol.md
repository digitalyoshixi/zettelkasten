---
tags:
  - networking
aliases:
  - SNMP
---
Protocol for:
- Collecting and monitoring metrics about devices on a network
- Syncing network clocks
Queries are sent and received `udp/161`
If a metric is monitored to be too high or too low, an trap (alert) can be sent to the management server.
Traps are sent and received over `udp/162`
# Concepts
- [[SNMP Agent]]
- [[SNMP Manager]]
- [[Management Information Base|MIB]]
- [[SNMP Trap]]
- [[Network Management System|NMS]]
# Versions
- [[SNMP V1]]
- [[SNMP V2]]
- [[SNMP V3]]