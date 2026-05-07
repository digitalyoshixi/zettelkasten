---
tags:
  - data
---
Will return all results in a table that is ordered by several keys where the order logic is:
- Order by first column 
- For duplicate first columns, order with second key if provided
- For duplicate first + second columns, order with third key if provided
- ...
# Alphabetic Ordering
```
SELECT col1, col2 FROM table_name ORDER BY col1, col2
```
# Descending Order
```
SELECT * FROM table_name ORDER BY column1 DESC
```
# Descending Order
```
SELECT * FROM table_name ORDER BY column1 ASC
```
# Order by Column Number
```
SELECT * FROM table_name ORDER BY 1
```
- Orders by columns 1