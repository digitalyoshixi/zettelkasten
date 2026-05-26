---
tags:
  - security
---
A [[Command and Control Server|C2]] that allows for easy development.
- Everything runs as a [[Docker]] container
# Installation
1. 
```
git clone https://github.com/its-a-feature/Mythic --depth 1 --single-branch
```
2. Have [[Docker]] or [[Orbstack]]
3. `make`
4. `mythic-cli install`
# Installing Extension
```
mythic-cli install folder /path/to/ext
```
# Running/Stopping
```
mythic-cli start
mythic-cli stop
```
# Guides
- [[Mythic GraphQL Docs]]