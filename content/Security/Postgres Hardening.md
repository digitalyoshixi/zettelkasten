---
tags:
  - database
  - security
  - database
---
[https://hackernoon.com/8-crucial-tips-for-hardening-postgresql-144-servers-in-2022](https://hackernoon.com/8-crucial-tips-for-hardening-postgresql-144-servers-in-2022)

1. Set listen_address to localhost. This will block connections from exterior networks
    
2. Lock down any ports other than database and management ports
    
3. Disable remote access in pg_hba.conf. Remote access is still possible if ssh to server then local connect
    
4. Hash data that you don't need reversed.
    
5. Create user groups
    
6. Enable query tracking for databases. Install pg_stat_statements extension first
    
7. Pg_basebackup or pgBackRest to create backups.