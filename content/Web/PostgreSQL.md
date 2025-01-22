---
tags:
  - database
---
An open-source relational [[Structured Query Language|SQL]] database 
# Postgres Setup Linux
1. `sudo pacman -S postgresql`
2. `sudo -u postgres -i`
3. `initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'`
4. `exit`
5. `sudo systemctl enable postgresql.service`
6. `sudo systemctl start postgresql.service`
7. `sudo -u postgres -i`
### Creating Database
1. `createdb <economy>`
2. `psql <databasename>`
3. `create role <user> with superuser login createdb;`
4. `\password <user>`
5. `set role <user>;`
6. `select current_user;`. you should be the \<user> now.
7. 
```
CREATE TABLE profiles (
	username VARCHAR(60) NOT NULL,
	password VARCHAR(60) NOT NULL,
	family_members INTEGER);
```
7. `INSERT INTO profiles values('david', '$2a$12$N88TysI0Kyz.l5TJlaHdbuuxPRt/5LoSJLqFqhYh2y2ksIAd2YtBe', 3);`
# Postgres Setup Windows
1. Install postgresql https://www.postgresql.org/download/
2. Add postgresql bin directory to PATH environment variable
   ![[PostgreSQL-20240803141906100.webp|421]]
# Other Methods to Setup
- [[Supabase]]