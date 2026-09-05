---
tags:
  - security
aliases:
  - SQLI View Columns
---
# View Tables [[MySQL]], [[PostgreSQL]], Microsoft
```
SELECT * FROM information_schema.tables
```
# View Columns Info [[MySQL]], [[PostgreSQL]], Microsoft
```
SELECT * FROM information_schema.columns WHERE table_name = 'users'
```
Returns something like:
```
TABLE_CATALOG TABLE_SCHEMA TABLE_NAME COLUMN_NAME DATA_TYPE ================================================================= MyDatabase dbo Users UserId int MyDatabase dbo Users Username varchar MyDatabase dbo Users Password varchar
```
### View Column Names
```
SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = 'users'
```