---
tags:
  - web
---
An [[Random Access Memory|RAM]] data structure storage used for:
- Databases
- [[Caching]]
- Message broking
![[Redis-20240802032649258.webp|237]]
Formatted like a [[JSON]] file
# Installation
```
sudo pacman -S redis
```
# Running
```
redis-server
```
Will run on port `6379`
```
redis-cli
```
# Commands
- [[Redis SET]]
- [[Redis SETEX]]
- [[Redis GET]]
- [[Redis DEL]]
- [[Redis EXISTS]]
- [[Redis KEYS]]
- [[Redis FLUSHALL]]
- [[Redis TTL]]
- [[Redis EXPIRE]]