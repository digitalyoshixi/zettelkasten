---
tags:
  - database
---
A [[Graph Database]] that is [[Atomicity Consistency Isolation Durability|ACID]] compliant.
# Installation
```
yay -S neo4j-desktop
```
# Running Local Database
1. `docker pull neo4j`
2. `docker run -d -p 7474:7474 -p 7687:7687 --env NEO4J_AUTH=<myuser>/<mypassword> neo4j:latest`
3. http://127.0.0.1:7474/browser, then login with your credentials
# Running with [[Neo4j Aura]]