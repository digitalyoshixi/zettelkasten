---
tags:
  - security
---
A [[Command and Control Server|C2]] that allows for easy development.
- Everything runs as a [[Docker]] container
# Architecture
![[Mythic-20260630163719903.webp]]
- Communicates with [[Remote Procedure Calls|RPC]] in [[RabbitMQ]]
- Docker container for the agent to accept RPC messages. Accepts:
	- Build requests to create a new mythic agent instance
- Task handler translation server to command (ls) -> encoded command for agent
- 
# Installation
1. 
```
git clone https://github.com/its-a-feature/Mythic --depth 1 --single-branch
```
2. Have [[Docker]] or [[Orbstack]]
3. `make`
4. `mythic-cli install`
# Installing/Removing Service
```
mythic-cli install folder /path/to/ext
mythic-cli uninstall servicename
```
# Running/Stopping
```
mythic-cli start
mythic-cli stop
```
# Guides
- [[Mythic GraphQL Docs]]