---
tags:
  - database
---
# Create a Table
```sql
CREATE TABLE table_name (
	column1 datatype,
	column2 datatype,
	column3 datatype
)
```
### Example
```sql
CREATE TABLE Persons (
	column_1 INTEGER NOT NULL,
	column_2 INTEGER,
    PRIMARY KEY(column_1)
);
```