---
tags:
  - windows
  - security
---
A tool used to scan a [[Windows Active Directory|AD]] network for all objects, users, etc.
# WebUI Installation
```
wget https://raw.githubusercontent.com/SpecterOps/BloodHound/refs/heads/main/examples/docker-compose/docker-compose.yml
```
```
docker compose up
```
- Note down the bloodhound admin password
- Go to http://127.0.0.1:8080
- `admin : <PASSWORD_YOU_COPIED>`
# Ingestors
- [[bloodhound-python]]
- [[rusthound]]