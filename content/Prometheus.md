---
tags:
  - devops
---
A [[Time-Series Database]] that stores [[Metrics]] of services.
Processes push to a gateway, and prometheus scrapes from that gateway.
![[Prometheus-20251029000033257.webp|355]]
# Installation
```
apt install prometheus
```
# Running
```
prometheus --config.file=prometheus.yml
```
# Concepts
- [[PromQL]]
	- [[PromQL count]]
- [[Prometheus Table]]
- [[Prometheus Graph]]
- [[prometheus config]]