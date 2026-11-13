---
tags:
  - security
  - database
---
A [[Stored Procedure]] that allows administrators to execute system commands directly via T-SQL.
```sql
exec master.dbo.xp_cmdshell
```

# Enabling
```
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
```