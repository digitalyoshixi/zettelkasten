---
tags:
  - security
---
1. https://github.com/CybercentreCanada/nte
2. Notice that the docker file contains:
```
services:
  nte-suricata:
    build:
      context: .
      dockerfile: docker/Dockerfile-suricata
    volumes:
      - ./pcaps:/data/pcaps
      - ./logs:/data/logs
      - ./INFECTED:/data/INFECTED
```
There are three volumes listed. One for network logs, one for IDS logs and one for infected? (presumably where malware samples go)

Notice that we are also using suricata, which is a intrusion prevention system. It alerts whenever there is malicious activity.

3. We take a look at logs first. In /logs there are two files:
- `eve.json.zst`
- `fast.log.zst`
According to suricata docs, eve.json is the larger full json representation of the logs and fast-log is the logs that are triggered during malicious activity.

We first try and view the fast-logs first:
- We must parse them into a indexable form for elastic. This requires us to go to the ai indexable portion.
- https://797c73251c80409cb43b3d374280ab08.us-central1.gcp.cloud.es.io/app/ml/filedatavisualizer
fast-logs have the form:
```
03/16/2012-12:30:00.090000  [**] [1:2024364:5] ET SCAN Possible Nmap User-Agent Observed [**] [Classification: Web Application Attack] [Priority: 1] {TCP} 192.168.202.79:50477 -> 192.168.229.251:80
```
I could not figure out the [[Grok Pattern]] to parse, and I'd already spent too much time on this. 
We will look manually later, for now we move onto the pcap files.
