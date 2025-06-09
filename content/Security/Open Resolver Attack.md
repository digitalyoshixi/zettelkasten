---
tags:
  - networking
  - security
aliases:
  - DNS Amplification Attack
---
A [[Smurf Attack]] [[Distributed Denial of Service|DDoS]] that involves sending spoofed packet of your victim as the source address to [[Domain Name Server|DNS]] resolver servers, that send large responses back.
Any DNS servers not configured to detect bad actors will participate in this attack, meaning all self-hosted DNS servers ([[Pi Hole]]) should be private.